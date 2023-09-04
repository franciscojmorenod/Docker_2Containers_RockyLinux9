import requests
import netifaces as ni
import os
#32e577853ea54906a84171559231908

class City_Weather:
    def __init__(self, xcity, xtemp, xcondition):
        self.city = xcity
        self.temp = xtemp
        self.condition = xcondition
    def __init__(self, xcity):
        self.city = xcity
        self.temp = "tbd"
        self.condition = "tbd"
    def JobOpportunities(self):
        res = "Lots of Jobs"
        return res

def get_weather(ycityObj):
    url = 'http://api.weatherapi.com/v1/current.json?key=32e577853ea54906a84171559231908&q='+ ycityObj.city + '&aqi=no'
    response = requests.get(url)
    weather_json = response.json()
    temp = weather_json.get('current').get('temp_f')
    condition = weather_json.get('current').get('condition').get('text')
    #print(weather_json)
    #print ("-------")
    ycityObj.condition = condition
    ycityObj.temp = temp
    
    return 


def os_command(xcmd):
    stream = os.popen(xcmd)
    output = stream.read()
    print(xcmd, '=', output)
    return

#   Main Program
input_city = "Tampa" # input('Enter City: ')
cityObj = City_Weather(input_city)
get_weather(cityObj)

print('Todays weather in ', cityObj.city , ' is', cityObj.condition, 'and', cityObj.temp, 'degrees')
print('Jobs Situation: ', cityObj.JobOpportunities())
print("------------------------------------------")

nis = ni.interfaces()

for nx in nis:
    print(nx, '=' , ni.ifaddresses(nx))
print("------------------------------------------")

os_command('cd ~')
os_command('pwd')
os_command('ls -la')
os_command('ifconfig')
os_command('netstat')
os_command('whoami')
# os_command("ping google.com")