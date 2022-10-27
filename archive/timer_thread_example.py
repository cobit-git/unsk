import time  
from threading import Timer  
def display(msg):  
    print(msg + ' ' + time.strftime('%H:%M:%S'))  
  
##Basic timer  
def run_once():  
    display('run_once:')  
    t=Timer(10,display,['Timeout:'])  
    t.start()#Here run is called  
run_once()  
##Runs immediately and once  
print('Waiting.....')  