import sys
import __builtin__
import resource
import signal
import os

#Process Memory, CPU Time, Maximum Physical Memeory
#Address Space, Opening Files must be restricted 

def resource_limitation():
    resource.setrlimit(resource.RLIMIT_RSS, (1024,1024)) # process memory
    resource.setrlimit(resource.RLIMIT_CPU, (1,4)) # CPU Cycle
    resource.setrlimit(resource.RLIMIT_MEMLOCK,(5000)) # Physical memory
    resource.setrlimit(resource.RLIMIT_AS, (1024)) # Address Space
    resource.setrlimit(resource.RLIMIT_OFFILE, (3)) # File Open Limitation

# Deleting functions in __builtin__ module
def function_deletion():
    del __builtin__.__dict__['abs']
    del __builtin__.__dict__['delattr']
    del __builtin__.__dict__['eval']
    del __builtin__.__dict__['exec']
    del __builtin__.__dict__['input']
    del __builtin__.__dict__['buffer']
 

# Coverting Special Characters by Excape Sequence
# idea from pyratemp sandbox implememtation
def symbol_conversion():
    if x== input("&"):
        x = x.replace( " &", "&amp;")
    if x == input("<"):
        x = x.replace("<", "&lt;")

    if x== input(">"):
        x = x.replace( " >", "&gt;")
  
    if x== input("'"):
        x = x.replace( " '", "&#39;")

# main Function

code = file(sys.argv[1]).read()
exec code
       
 

        


                 

    
    




        
    
    


    





    






