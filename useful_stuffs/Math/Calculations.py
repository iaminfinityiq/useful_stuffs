def find_percentage(percentage_type: int, num1: float, num2: float) -> float:
  """
  Returns the result based on 3 calculation types based on the percentage_type parameter.
  """
  if type(num1) is not float and type(num1) is not int:
    import useful_stuffs.IO
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"num1 requires float | int, not {useful_stuffs.IO.return_type(num1)}")
  if type(num2) is not float and type(num2) is not int:
    import useful_stuffs.IO
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"num2 requires float | int, not {useful_stuffs.IO.return_type(num2)}")

  match percentage_type:
    case 0:
      # Find num2% of num1
      return num1 * (num2 / 100)
    case 1:
      # Find x when num2% of x is num1
      return num1 / (num2 / 100)
    case 2:
      # Find x when x% of num1 is num2 (return %)
      return num2 / num1 * 100
    case _:
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(percentage_type) is not int:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"percentage_type requires int, not {useful_stuffs.Strings.return_type(percentage_type)}")
      elif percentage_type < 0 and percentage_type > 2:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""percentage_type can only receive values of 1, 2 and 3, not {percentage_type}
If percentage_type is 0, you find num2% of num1
If percentage_type is 1, you find x when num2% of x is num1
If percentage_type is 2, you find x when x% of num1 is num2 (remember, it returns %)""")

def factorial(num: int) -> int:
  """
  Calculates the factorial of a given number
  """
  if type(num) is not int:
    import useful_stuffs.Strings
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"num requires int, not {useful_stuffs.Strings.return_type(num)}")
  if num < 0:
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.InvalidInputError(f"Can't find factorial of {num} ({num}!) because {num} is < 0")
  if num == 0 or num == 1:
    return 1
  else:
    return num * factorial(num - 1)
