"""
Helps you in daily "programming" life
"""
def include(module: str) -> None:
  """
  Includes all modules in useful_stuffs needed.
  """
  match module.lower():
      case "math":
          import useful_stuffs.Math
      case "io":
          import useful_stuffs.IO
      case "input/output":
          import useful_stuffs.IO
      case "error":
          import useful_stuffs.Errors
      case _:
          import useful_stuffs.IO
          import useful_stuffs.Errors
          if type(module) is not str:
              raise useful_stuffs.Errors.NoTypeMatchedError(f"module requires str, not {useful_stuffs.IO.return_type(module)}")
          else:
              raise useful_stuffs.Errors.NoValueMatchedError(f"""No inputs defined {module.lower()} in useful_stuffs
All inputs defined available in useful_stuffs are as followings:
1. math: imports useful_stuffs.Math
2. io: imports useful_stuffs.IO
3. input/output: imports useful_stuffs.IO
Remember: input/output is one thing, not 2 seperate things (input and output)!""")
