def convert_length(starting_number: float | int, starting_unit: str, result_unit: str) -> float | int:
  """
  Convert from starting_unit to result_unit (length)
  """
  if type(starting_number) is not float and type(starting_number) is not int:
    import useful_stuffs.IO
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_number requires float | int, not {useful_stuffs.IO.return_type(starting_number)}")

  match starting_unit:
    case "km":
      result = starting_number * 100000
    case "hm":
      result = starting_number * 10000
    case "dam":
      result = starting_number * 1000
    case "m":
      result = starting_number * 100
    case "dm":
      result = starting_number * 10
    case "cm":
      result = starting_number
    case "mm":
      result = starting_number / 10
    case "µm":
      result = starting_number / 10000
    case "micrometer":
      result = starting_number / 10000
    case "nm":
      result = starting_number / 10000000
    case "mile":
      result = starting_number * 160935
    case "yd":
      result = starting_number * 91.44
    case "ft":
      result = starting_number * 30.48
    case "inch":
      result = starting_number * 2.54
    case "light year":
      result = starting_number * 946066000000000000
    case _:
      import useful_stuffs.IO
      import useful_stuffs.Errors
      if type(starting_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.IO.return_type(starting_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No length unit available named: {starting_unit}
All length units that are available are:
1. km (1 km = 100000 cm)
2. hm (1 hm = 10000 cm)
3. dam (1 dam = 1000 cm)
4. m (1 m = 100 cm)
5. dm (1 dm = 10 cm)
6. cm
7. mm (1 mm = 1/10 cm)
8. µm/micrometer (1 µm = 1/10000 cm)
9. nm (1 nm = 1/10000000 cm)
10. mile (1 mile = 160935 cm)
11. yd (1 yd = 91.44 cm)
12. ft (1 ft = 30.48)
13. inch (1 inch = 2.54 cm)
14. light year (1 light year = 946066000000000000 cm)""")

  match result_unit:
    case "km":
      return result / 100000
    case "hm":
      return result / 10000
    case "dam":
      return result / 1000
    case "m":
      return result / 100
    case "dm":
      return result / 10
    case "cm":
      return result
    case "mm":
      return result * 10
    case "µm":
      return result * 10000
    case "micrometer":
      return result * 10000
    case "nm":
      return result * 10000000
    case "mile":
      return result / 160935
    case "yd":
      return result / 91.44
    case "ft":
      return result / 30.48
    case "inch":
      return result / 2.54
    case "light year":
      return result / 946066000000000000
    case _:
      import useful_stuffs.IO
      import useful_stuffs.Errors
      if type(result_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"result_unit requires str, not {useful_stuffs.IO.return_type(result_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No length unit available named: {result_unit}
All length units that are available are:
1. km (1 km = 100000 cm)
2. hm (1 hm = 10000 cm)
3. dam (1 dam = 1000 cm)
4. m (1 m = 100 cm)
5. dm (1 dm = 10 cm)
6. cm
7. mm (1 mm = 1/10 cm)
8. µm/micrometer (1 µm = 1/10000 cm)
9. nm (1 nm = 1/10000000 cm)
10. mile (1 mile = 160935 cm)
11. yd (1 yd = 91.44 cm)
12. ft (1 ft = 30.48)
13. inch (1 inch = 2.54 cm)
14. light year (1 light year = 946066000000000000 cm)""")

def convert_temperature(starting_number: float | int, starting_unit: str, result_unit: str) -> float | int:
  """
  Convert from starting_unit to result_unit (temperature)
  """
  if type(starting_number) is not float and type(starting_number) is not int:
    import useful_stuffs.IO
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_number requires float | int, not {useful_stuffs.IO.return_type(starting_number)}")

  match starting_unit:
    case "°C":
      result = starting_number
    case "celsius":
      result = starting_number
    case "°F":
      result = (starting_number - 32) / 1.8
    case "fahrenheit":
      result = (starting_number - 32) / 1.8
    case "K":
      result = starting_number - 273.15
    case "kelvin":
      result = starting_number - 273.15
    case _:
      import useful_stuffs.IO
      import useful_stuffs.Errors
      if type(starting_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.IO.return_type(starting_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No temperature unit available named: {starting_unit}
All temperature units that are available are:
1. °C/celsius
2. °F/fahrenheit ((°F - 32) / 1.8 = °C)
3. K/kelvin (K - 273.15 = C)""")

  match result_unit:
    case "°C":
      return result
    case "celsius":
      return result
    case "°F":
      return result * 1.8 + 32
    case "fahrenheit":
      return result * 1.8 + 32
    case "K":
      return result + 273.15
    case "kelvin":
      return result + 273.15
    case _:
      import useful_stuffs.IO
      import useful_stuffs.Errors
      if type(result_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"result_unit requires str, not {useful_stuffs.IO.return_type(result_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No temperature unit available named: {result_unit}
All temperature units that are available are:
1. °C/celsius
2. °F/fahrenheit ((°F - 32) / 1.8 = °C)
3. K/kelvin (K - 273.15 = C)""")
