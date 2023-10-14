import requests
import base64

url = "http://chal.ctf.games:31903/"

header = {
  "Authorization": "Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg=="
}

request = requests.get(url, headers=header)
print(base64.b64decode(request.text.replace(" -->", "").replace("<!-- ", "")).decode())