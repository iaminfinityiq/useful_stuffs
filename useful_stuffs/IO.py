"""
Includes all of the functions you need for inputs and outputs.
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
