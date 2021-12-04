import os

WORKDIR = os.path.dirname(os.path.dirname(__file__) + '..')

from .check_license import checkLicense
from .get_hardware import getHardwareData

def authenticate(func):
    def wrapper(*args, **kwargs):     
        path_to_license = os.path.join(WORKDIR, 'license.txt')
        currentHardware = str(getHardwareData())
        
        if checkLicense(path_to_license, currentHardware):
            func(*args, **kwargs)
            
    return wrapper
