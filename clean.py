import requests
import json
from itertools import zip_longest
import difflib
import yaml
import re
import time
import datetime
import calendar


from auth_header import Authentication as auth
from operations import Operation
from clean_class import getData
from clean_class import deleteData
#from clean_class import parseData



if __name__=='__main__':

    while True:

        """ open the yaml file where the constant data is stored"""

        with open("vmanage_login1.yaml") as f:
            config = yaml.safe_load(f.read())


        """ extracting info from Yaml file"""

        vmanage_host = config['vmanage_host']
        vmanage_port = config['vmanage_port']
        username = config['vmanage_username']
        password = config['vmanage_password']
        
        year =  config['year']
        month = config['month']
        day = config['day']
        hour = config['hour']
        minutes = config['minutes']
        seconds = config['seconds']
        


        """ GET the TOKEN from Authnetication call"""
        header= auth.get_header(vmanage_host, vmanage_port,username, password)
        
        epochTime = int(datetime.datetime(year, month, day, hour, minutes, seconds).strftime('%s'))*1000
        

        """ Extrat and delete Device Template ID which is not attached to any device and not factory default"""

        deviceTemplate = getData.getDeviceTemplate(vmanage_host,vmanage_port,header)
        for iter_deviceTemplate in deviceTemplate:
            if (iter_deviceTemplate["factoryDefault"] == False and iter_deviceTemplate["devicesAttached"] == 0) and iter_deviceTemplate["lastUpdatedOn"] < epochTime:
                res = deleteData.deleteDeviceTemplate(vmanage_host,vmanage_port,header,iter_deviceTemplate["templateId"])
                print(f' Deleted Device Template - {iter_deviceTemplate["templateName"]} ') if res.status_code == 200 else print("unable to delete")

        """ Extrat and delete feature Template ID which is not attached to any device and not factory default"""

        featureTemplate = getData.getFeatureTemplate(vmanage_host,vmanage_port,header)
        for iter_featureTemplate in featureTemplate:
            if (iter_featureTemplate["factoryDefault"] == False and iter_featureTemplate["devicesAttached"] == 0) and iter_featureTemplate["lastUpdatedOn"] < epochTime:
                res = deleteData.deleteFeatureTemplate(vmanage_host,vmanage_port,header,iter_featureTemplate["templateId"])
                print(f' Deleted feature Tempalte - {iter_featureTemplate["templateName"]} ') if res.status_code == 200 else print("unable to delete")



        exit()
