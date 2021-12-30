import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.control import Control

if __name__ == '__main__':

    run = Control()
    run.search_article()