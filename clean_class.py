"""
import all the reqiured librariers
"""
import requests
import json
import difflib
import yaml
import re
import time


from auth_header import Authentication as auth
from operations import Operation




class getData():
    """
    Get info of Device and feature Template
    """

    def getDeviceTemplate(vmanage_host,vmanage_port,header):

        api_Device_Template = '/dataservice/template/device?feature=lawful-interception'
        url_Device_Template = Operation.url(vmanage_host,vmanage_port,api_Device_Template)
        Device_Template = Operation.get_method(url_Device_Template,header)
        return Device_Template['data']

    def getFeatureTemplate(vmanage_host,vmanage_port,header):

        api_Feature_Template = '/dataservice/template/feature?summary=false'
        url_Feature_Template = Operation.url(vmanage_host,vmanage_port,api_Feature_Template)
        Feature_Template = Operation.get_method(url_Feature_Template,header)
        return Feature_Template['data']




class deleteData():

    """
    Delete the Device and Feature template
    """

    def deleteDeviceTemplate(vmanage_host,vmanage_port,header,deviceTemplateID):
        api_delete_Device_template = f'/dataservice/template/device/{deviceTemplateID}'
        url_delete_Device_template = Operation.url(vmanage_host,vmanage_port,api_delete_Device_template)
        data_delete_Device_template = Operation.delete_method(url_delete_Device_template,header)
        return data_delete_Device_template

    def deleteFeatureTemplate(vmanage_host,vmanage_port,header,featureTemplateID):
        api_delete_Feature_template = f'/dataservice/template/feature/{featureTemplateID}'
        url_delete_Feature_template = Operation.url(vmanage_host,vmanage_port,api_delete_Feature_template)
        data_delete_Feature_template = Operation.delete_method(url_delete_Feature_template,header)
        return data_delete_Feature_template
