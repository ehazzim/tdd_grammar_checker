## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

def check_grammar(text):

    Parameters:
        text: str - a string representing a sentence or text to check

    Returns:
        bool - True if text starts with an uppercase letter AND ends with 
               a valid punctuation mark ('.', '!', '?'); False otherwise

    Side effects:
        None

    Raises:
        TypeError: If `text` is not a string
        ValueError: If `text` is an empty string

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
1. Valid inputs (Return True)
"""
# "Hello, world." -> True
# "That's awesome!" -> True

"""
2. Invalid start character (Return False)
"""
# "hello, world." -> False (starts with lowercase)
# "123 Hello." -> False (starts with digit, not capital letter)

"""
3. Invalid end character (Return False)
"""
# "Hello, world" -> False (missing punctuation)
# "Hello, world," -> False (ends with comma, not sentence-ending mark)

"""
4. Both invalid (Return False)
"""
# "hello world" -> False

"""
5. Edge Cases & Errors (Raise Exceptions)
"""
# "" (empty string) -> raises ValueError("Text cannot be empty")
# 12345 (non-string input) -> raises TypeError("Input must be a string")
```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

import pytest
from lib.grammar_checker import check_grammar

def test_valid_sentence_with_period():
    assert check_grammar("Hello, world.") == True

def test_valid_sentence_with_question_mark():
    assert check_grammar("How are you?") == True

def test_valid_sentence_with_exclamation_mark():
    assert check_grammar("This is great!") == True

def test_lowercase_first_letter_returns_false():
    assert check_grammar("hello, world.") == False

def test_missing_ending_punctuation_returns_false():
    assert check_grammar("Hello, world") == False

def test_invalid_ending_punctuation_returns_false():
    assert check_grammar("Hello, world,") == False

def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        check_grammar("")

def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        check_grammar(12345)
```

Ensure all test function names are unique, otherwise pytest will ignore them!