## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

def grammar_checker(text):

    Parameters: (list all parameters and their types)
        text: a string containing words that start with capital letter and end with
        suitable punctuation mark

    Returns: (state the return value and its type)
        a boolean value determining whether grammar correct (True) or incorrect
        (False)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given text with a string of words and punctuation
mark, return True
"""


"""
Given text where first letter lowercase, return False
"""

"""
If text has no punctuation mark at end, return False
"""

"""
Throw an error if no string is inputted
"""

"""
If type of text is not string, throw an error
"""

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.grammer_checker import *

"""
Given text with a string of words and punctuation
mark, return True
"""
def test_correct_input():
    pass
```

Ensure all test function names are unique, otherwise pytest will ignore them!