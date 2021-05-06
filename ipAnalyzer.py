from urllib.request import urlopen
import os
import IP2Location
import IP2Proxy
import geoip2.database
import IP2Proxy
import sys
import requests
import maxminddb
import pandas as pd
import datetime
from zipfile import ZipFile

def remove_entersFromAndMakeList(ip_list):
    for i in range(len(ip_list)):
        ip = ip_list[i]
        ip = ip.replace('\n', '')
        ip_list[i] = [ip]


def functionToFilter(text):
    return "ExitAddress" in str(text)  # returns if the text Contains ExitAddress


def generateTorIpDB():
    request = requests.get("https://www.dan.me.uk/torlist/?exit")
    if request.status_code==200:
        fechaActual = datetime.datetime.now()
        with open('data/registroFechas.txt', 'a') as writer:
            writer.write("\n" + str(fechaActual))
        writer.close()
        with open('data/nodosTor.txt', 'w') as writer:
            writer.write(request.text)
        writer.close()
    tor_api = open(os.path.join("data", "nodosTor.txt"))
    tor_database = tor_api.readlines()
    #db to validate tor nodes
    for i in range(len(tor_database)):
        ip = tor_database[i]
        tor_database[i] = ip.replace('\n', '')
    tor_api = urlopen('https://check.torproject.org/exit-addresses')
    tor_validationdb = tor_api.readlines()
    tor_validationdb = list(filter(functionToFilter, tor_validationdb))
    for index in range(len(tor_validationdb)):
        ip = tor_validationdb[index]
        ip = str(ip).split(" ")[1]
        tor_validationdb[index] = ip
    return tor_database,tor_validationdb


def locationOf(ip):
    with geoip2.database.Reader('data/geolocalizar/dbip-country-lite-2021-04.mmdb') as db:
        try:
            full_answer = db.country(ip)# {'ip': '172.217.172.110', 'country_short': 'US', 'country_long': 'United States'}
            location = full_answer.country.name
        except:
            location="N/A"
    db.close()
    with geoip2.database.Reader('data/geolocalizar/GeoLite2-Country.mmdb') as database2:
       try:
        consulta = database2.country(ip)
        verificacion = consulta.country.name
       except:
           verificacion="N/A"
    database2.close()

    #verificacion = location
    return location if verificacion == location else "N/A"


def proxyOf(ip):
    database = IP2Proxy.IP2Proxy()
    database.open(os.path.join("data/proxy_tor", "IP2PROXY-LITE-PX2.BIN"))
    full_answer = database.get_all(ip)  # {'is_proxy': 0, 'proxy_type': '-'}
    is_proxy = full_answer['is_proxy'] == True
    return is_proxy

def asnOf(ip):
    organizationName="N/A"
    with geoip2.database.Reader('data/asn/GeoLite2-ASN.mmdb') as db:
        try:
            full_response=db.asn(ip)
            organizationName = full_response.autonomous_system_organization
            asn= full_response.autonomous_system_number
        except:
            asn="N/A"
    db.close()

    with maxminddb.open_database(('data/asn/dbip-asn-lite-2021-04.mmdb')) as db2:
        try:
            full_response = db2.get(ip)
            validation = full_response['autonomous_system_number']
        except:
            validation = "N/A"
    db2.close()

    #validation = asn
    return organizationName if asn==validation else "N/A"

def checkTorNode(ip):
    return ip in tor_database and ip in tor_validation
    #return ip in tor_database


def getIPListFrom(file_to_analyze):
    file = open(file_to_analyze, 'r')
    ip_list = file.readlines()
    remove_entersFromAndMakeList(ip_list)
    return ip_list


class IPAnalyzer():

    def __init__(self, file_to_analyze):
         if file_to_analyze != "":
            self.fileToAnalyze = file_to_analyze
            self.iPList = getIPListFrom(file_to_analyze)
            self.processIpList()

    def findLocationOfIpList(self):
        ip_list = self.iPList
        for ip in ip_list:
            location = locationOf(ip[0])
            ip.append(location)

    def checkTorNodeOfIpList(self):
        ip_list = self.iPList
        for ip in ip_list:
            tor_node = str(checkTorNode(ip[0], tor_database))
            ip.append(tor_node)

    def getIPList(self):
        return self.iPList

    def checkProxyOfIpList(self):
        ip_list = self.iPList
        for ip in ip_list:
            is_proxy = proxyOf(ip[0])
            ip.append(is_proxy)

    def processIpList(self):
        ip_list = self.iPList
        i=0
        for ip in ip_list:
            location = locationOf(ip[0])
            is_proxy = proxyOf(ip[0])
            tor_node = str(checkTorNode(ip[0]))
            asn=asnOf(ip[0])

            ip.append(location)
            ip.append(is_proxy)
            ip.append(tor_node)
            ip.append(asn)


with ZipFile('data.zip', 'r') as zipObj:
    zipObj.extractall()
    tor_database,tor_validation = generateTorIpDB()