import os
import sys 

WORKDIR = os.path.dirname(__file__)
sys.path.append( WORKDIR )

from src.check_license import checkLicense

def authenticate(func):
    def wrapper(*args, **kwargs):     
        path_to_license = os.path.join(WORKDIR, 'store/license.txt')

        if checkLicense(path_to_license):
            func(*args, **kwargs)
            
    return wrapper
