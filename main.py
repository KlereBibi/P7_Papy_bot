
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.app import controller

if __name__ == '__main__':
    
    run = controller()
    run.home()
