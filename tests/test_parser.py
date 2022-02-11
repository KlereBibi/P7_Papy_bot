""" this module is the test of methode parser in class InputParser """

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.entities.inputparser import InputParser

def test_return_str_parser():
    user_question = "j'ai mangé des CHIPS, c'était avant hier!"
    sut = InputParser()
    excepted_value = "mange+chips"
    assert sut.parser(user_question) == excepted_value
