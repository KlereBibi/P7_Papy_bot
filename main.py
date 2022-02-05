"""This module contains the main function of the application"""
import os
from app import create_app

if __name__ == '__main__':
    app = create_app({"TESTING": False})
    port = int(os.getenv('PORT'))
    app.run(port=port)