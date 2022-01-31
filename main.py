import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app import create_app

app = create_app({"TESTING": False})

if __name__ == '__main__':
    app.run()

