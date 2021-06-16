import logging
import datetime
import requests

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = "https://localhost:15716/hello"

def run():
  
  a = datetime.datetime.now()
  
  # open session
  session = requests.session()

  x = range(1000)
  for n in x:
    #response = requests.request("POST", url, verify=False, json={"name": "Mauro"})
    response = session.request("POST", url, verify=False, json={"name": "Mauro"})
    print("Greeter client received: " + response.json()["message"])

    #response = requests.request("POST", url, verify=False, json={"name": "Savi"})
    response = session.request("POST", url, verify=False, json={"name": "Savi"})
    print("Greeter client received: " + response.json()["message"])

  b = datetime.datetime.now()
  print(b-a)

if __name__ == '__main__':
    logging.basicConfig()
    run()