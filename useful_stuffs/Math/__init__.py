"""
Includes all of the functions you need for Math
"""
def include(module: str):
  """
  Includes all modules in useful_stuffs.Math needed
  """
  match module.lower():
    case "calculation":
      import useful_stuffs.Math.Calculations
    case "equation":
      import useful_stuffs.Math.Calculations
    case "formula":
      import useful_stuffs.Math.Calculations
    case "conversion":
      import useful_stuffs.Math.Conversions
    case _:
      import useful_stuffs.Errors
      import useful_stuffs.IO
      if type(module) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"""module requires str, not {useful_stuffs.IO.return_type(module)}""")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No inputs defined {module.lower()} in useful_stuffs.Math
All of the inputs defined available in useful_stuffs.Math are as followings:
1. calculation/equation imports useful_stuffs.Math.Calculations
2. conversion imports useful_stuffs.Math.Conversions
Case sensitive is not used.""")
