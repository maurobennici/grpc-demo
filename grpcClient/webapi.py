import logging
import datetime
import requests

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url1 = "https://localhost:15716/hello/?name=Mauro"
url2 = "https://localhost:15716/hello/?name=Savi"



def run():
  
  a = datetime.datetime.now()

  # open session
  session = requests.session()
  
  x = range(1000)
  for n in x:
    #response = requests.request("GET", url1, verify=False)
    response = session.request("GET", url1, verify=False)
    print("Greeter client received: " + response.text)

    #response = requests.request("GET", url2, verify=False)
    response = session.request("GET", url2, verify=False)
    print("Greeter client received: " + response.text)

  b = datetime.datetime.now()
  print(b-a)

if __name__ == '__main__':
    logging.basicConfig()
    run()