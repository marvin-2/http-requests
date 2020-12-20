import json
import requests

def get():
  # Parameters
  ploads = {'things':2,'total':25}
  r = requests.get('https://httpbin.org/get',params=ploads)
  print(r.text)
  print()
  print(r.url)
  print()
  print(r.content)
  print()
  print(r.json)

def get2(toPath):
  # Perform HTTP GET request
  r = requests.get('https://api.github.com/events')

  # Save json response to output file
  with open(toPath, 'w') as jsonF:
    jsonF.write(json.dumps(r.json(), indent=4))