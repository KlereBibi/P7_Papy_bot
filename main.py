"""This module contains the main function of the application"""

from app import create_app

if __name__ == '__main__':
    app = create_app({"TESTING": False})
    app.run()