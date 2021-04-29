from urllib.request import urlopen
import os
import IP2Location


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
    tor_api = urlopen('https://check.torproject.org/exit-addresses')
    tor_database = tor_api.readlines()
    tor_database = list(filter(functionToFilter, tor_database))
    for index in range(len(tor_database)):
        ip = tor_database[index]
        ip = str(ip).split(" ")[1]
        tor_database[index] = ip
        print(ip)
    return tor_database


def locationOf(ip):
    database = IP2Location.IP2Location()
    database.open(os.path.join("data", "IP-COUNTRY.BIN"))
    full_answer = database.get_all(
        ip)  # {'ip': '172.217.172.110', 'country_short': 'US', 'country_long': 'United States'}
    location = full_answer.country_long
    return location


def checkTorNode(ip, tor_database):
    for ip_tor in tor_database:
        if ip == ip_tor:
            return True
    return False


def getIPListFrom(file_to_analyze):
    file = open(file_to_analyze, 'r')
    ip_list = file.readlines()
    remove_entersFromAndMakeList(ip_list)
    return ip_list


class IPAnalyzer():
    def __init__(self, file_to_analyze):
        self.fileToAnalyze = file_to_analyze
        self.iPList = getIPListFrom(file_to_analyze)
        self.findLocationOfIpList()
        self.checkTorNodeOfIpList()

    def findLocationOfIpList(self):
        ip_list = self.iPList
        for ip in ip_list:
            location = locationOf(ip[0])
            ip.append(location)

    def checkTorNodeOfIpList(self):
        ip_list = self.iPList
        tor_database = generateTorIpDB()
        for ip in ip_list:
            tor_node = str(checkTorNode(ip[0], tor_database))
            ip.append(tor_node)

    def getIPList(self):
        return self.iPList