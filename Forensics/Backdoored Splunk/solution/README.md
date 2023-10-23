# Backdoored Splunk - Forensics Challenge

## Basic Information
**Name:** Backdoored Splunk  
**Category:** Forensics  
**Points:** 50

## Objective

The "Backdoored Splunk" challenge is a forensics task that involves examining a web instance. Your objective is to access the web instance and uncover the hidden flag, which is encoded in Base64. To achieve this, you need to modify the HTTP headers to gain access.

## Solution

To successfully complete the "Backdoored Splunk" forensics challenge, follow these steps:

1. **Access the Web Instance:**
   - Start by opening the provided web instance. Upon accessing it, you may encounter an error or notice that additional headers are required for access.
![Website](website.png)

2. **Search Downloaded Challenge Folder:**
   - I thought it was an error, but it was mentioned by Huntress CTF that this behaviour is intended. We have to find which headers are required for this to work
   - I immediately searched the downloaded challenge folder for headers
![Headers](<requires header.png>)
   - This shows that it requires an authorisation header

3. **Modify the Header Using Burp Suite:**
   - Modify the HTTP headers of your requests using a tool like Burp Suite.
   - Or alternatively, you can write a python script that does this for you.
      ```python
      import requests
      import base64

      url = "http://chal.ctf.games:31903/"

      header = {
        "Authorization": "Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg=="
      }

      request = requests.get(url, headers=header)
      print(base64.b64decode(request.text.replace(" -->", "").replace("<!-- ", "")).decode())
      ```

4. **Access the Website with Modified Headers:**
   - With the modified headers, access the website again. You should now be able to view the content without errors or restrictions.

5. **Locate and Decode the Flag:**
   - After gaining access to the content, search for the flag. In this case, the flag is encoded in Base64. Look for the Base64-encoded string within the web instance.

6. **Decode the Base64 Flag:**
   - Once you find the Base64-encoded flag, use an online Base64 decoder or a programming language to decode the string and reveal the actual flag.

Flag: flag{XXXXXXXXXX}

**Challenge Solved**  
