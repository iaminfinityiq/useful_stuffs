"""
Includes extra errors that can happen when you program using useful_stuffs
"""
class NoValueMatchedError(Exception):
    """
    No inputs matched the following inputs defined in the function.
    """

class NoTypeMatchedError(Exception):
    """
    No types of inputs matched the following types of inputs defined in the function
    """

class InvalidInputError(Exception):
    """
    The inputs are invalid.
    """