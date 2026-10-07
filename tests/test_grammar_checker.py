import pytest
from lib.grammar_checker import *

def test_valid_inputs():
    result = grammar_checker("Hello world!")
    assert result == True

def test_invalid_start_char():
    result = grammar_checker("hello world.")
    assert result == False

def test_invalid_end_punctuation():
    result = grammar_checker("Hello world")
    assert result == False

def test_start_end_invalid():
    result = grammar_checker("hello world")
    assert result == False