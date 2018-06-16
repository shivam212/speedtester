import sys
import requests
import time
t1=time.time()
file=requests.get("http://speedtest.ftp.otenet.gr/files/test10Mb.db")
file.raise_for_status()
t2=time.time()
diff=t2-t1
print(t2,t1)
speed=(10*1024)/(diff)
print(f'The download speed is {speed} KB/s, {speed/1024} MB/s, {8*(speed)/1024} Mbps')