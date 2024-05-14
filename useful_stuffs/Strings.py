"""
Includes all of the functions you need if you are working with strings.
"""
def return_type(value) -> str:
  """
  Helps you get the neater value of the type. For example: return_type("Hello World") returns str
  """
  string_type = str(type(value))
  type_ = ""
  for i, c in enumerate(string_type):
    if i < len("<class '") or i >= len(string_type) - len("'>"):
      continue

    type_ += c

  return type_

def count_capitals(value: str) -> int:
  """
  Counts how many capital letters that are in the given string
  """
  if type(value) is not str:
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"value requires str, not {return_type(value)}")
  new_string = value.lower()
  result = 0
  for i, c in enumerate(new_string):
    if c != value[i]:
      result += 1

  return result

def count_lowers(value: str) -> int:
  """
  Counts how many lower letters that are in the given string
  """
  if type(value) is not str:
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"value requires str, not {return_type(value)}")
  new_string = value.upper()
  result = 0
  for i, c in enumerate(new_string):
    if c != value[i]:
      result += 1

  return result
