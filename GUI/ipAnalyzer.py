from urllib.request import urlopen
import os
import IP2Location
import IP2Proxy


def remove_entersFromAndMakeList(ip_list):
    for i in range(len(ip_list)):
        ip = ip_list[i]
        ip = ip.replace('\n', '')
        ip_list[i] = [ip]


'''
def locationOf(ip):
    api_key = 'your_api_key'
    api_url = 'https://geo.ipify.org/api/v1?'
    url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
    location = urlopen(url).read().decode('utf8')
    #location = 'bsas'
    print(location)
    return location
'''


def functionToFilter(text):
    return "ExitAddress" in str(text)  # returns if the text Contains ExitAddress


def generateTorIpDB():
    # La api funciona cada 30 min, puse todo en un archivo para poder hacer pruebas                                                                                                                                         .
    # tor_api = urlopen("https://www.dan.me.uk/torlist/?exit")
    tor_api = open(os.path.join("data", "torIps.txt"))
    tor_database = tor_api.readlines()
    for i in range(len(tor_database)):
        ip = tor_database[i]
        tor_database[i] = ip.replace('\n', '')
    return tor_database


def locationOf(ip):
    database = IP2Location.IP2Location()
    database.open(os.path.join("data", "IP-COUNTRY.BIN"))
    full_answer = database.get_all(ip)
    # {'ip': '172.217.172.110', 'country_short': 'US', 'country_long': 'United States'}
    location = full_answer.country_long
    return location


def proxyOf(ip):
    database = IP2Proxy.IP2Proxy()
    database.open(os.path.join("data", "IP2PROXY-LITE-PX2.BIN"))
    full_answer = database.get_all(ip)  # {'is_proxy': 0, 'proxy_type': '-'}
    is_proxy = full_answer['is_proxy'] == True
    return is_proxy


def checkTorNode(ip, tor_database):
    return ip in tor_database


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
            self.findLocationOfIpList()
            self.checkTorNodeOfIpList()
						self.checkProxyOfIpList()

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




tor_database = generateTorIpDB()
