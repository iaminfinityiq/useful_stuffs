def convert_length(starting_number: float | int, starting_unit: str, result_unit: str) -> float | int:
  """
  Convert from starting_unit to result_unit (length)
  """
  if type(starting_number) is not float and type(starting_number) is not int:
    import useful_stuffs.Strings
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_number requires float | int, not {useful_stuffs.Strings.return_type(starting_number)}")

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
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(starting_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.Strings.return_type(starting_unit)}")
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
12. ft (1 ft = 30.48 cm)
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
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(result_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"result_unit requires str, not {useful_stuffs.Strings.return_type(result_unit)}")
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
12. ft (1 ft = 30.48 cm)
13. inch (1 inch = 2.54 cm)
14. light year (1 light year = 946066000000000000 cm)""")

def convert_temperature(starting_number: float | int, starting_unit: str, result_unit: str) -> float | int:
  """
  Convert from starting_unit to result_unit (temperature)
  """
  if type(starting_number) is not float and type(starting_number) is not int:
    import useful_stuffs.Strings
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_number requires float | int, not {useful_stuffs.Strings.return_type(starting_number)}")

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
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(starting_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.Strings.return_type(starting_unit)}")
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
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(result_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"result_unit requires str, not {useful_stuffs.Strings.return_type(result_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No temperature unit available named: {result_unit}
All temperature units that are available are:
1. °C/celsius
2. °F/fahrenheit ((°F - 32) / 1.8 = °C)
3. K/kelvin (K - 273.15 = C)""")

def convert_area(starting_number: float | int, starting_unit: str, result_unit: str):
  """
  Convert from starting_unit to result_unit (area)
  """
  if type(starting_number) is not float and type(starting_number) is not int:
    import useful_stuffs.Strings
    import useful_stuffs.Errors
    raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_number requires float | int, not {useful_stuffs.Strings.return_type(starting_number)}")
    
  match starting_unit:
    case "km2":
      result = starting_number * 100000 ** 2
    case "hm2":
      result = starting_number * 10000 ** 2
    case "dam2":
      result = starting_number * 1000 ** 2
    case "m2":
      result = starting_number * 100 ** 2
    case "dm2":
      result = starting_number * 10 ** 2
    case "cm2":
      result = starting_number
    case "mm2":
      result = starting_number / 10 ** 2
    case "µm2":
      result = starting_number / 10000 ** 2
    case "square micrometer":
      result = starting_number / 10000 ** 2
    case "nm2":
      result = starting_number / 10000000 ** 2
    case "square mile":
      result = starting_number * 160935 ** 2
    case "yd2":
      result = starting_number * 91.44 ** 2
    case "ft2":
      result = starting_number * 30.48 ** 2
    case "inch2":
      result = starting_number * 2.54 ** 2
    case "square light year":
      result = starting_number * 946066000000000000 ** 2
    case _:
      import useful_stuffs.Strings
      import useful_stuffs.Errors
      if type(starting_unit) is not str:
        raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.Strings.return_type(starting_unit)}")
      else:
        raise useful_stuffs.Errors.NoValueMatchedError(f"""No area unit available named: {starting_unit}
All area units that are available are:
1. km2 (1 km2 = 10000000000 cm2)
2. hm2 (1 hm2 = 100000000 cm2)
3. dam2 (1 dam2 = 1000000 cm2)
4. m2 (1 m2 = 10000 cm2)
5. dm2 (1 dm2 = 100 cm2)
6. cm2
7. mm2 (1 mm2 = 1/100 cm2)
8. µm2/square micrometer (1 µm2 = 1/100000000 cm2)
9. nm2 (1 nm2 = 1/100000000000000 cm2)
10. square mile (1 square mile = 25900074225 cm2)
11. yd2 (1 yd2 = 8361.2736 cm2)
12. ft2 (1 ft2 = 929.0304 cm2)
13. inch2 (1 inch2 = 6.4516 cm2)
14. square light year (1 square light year = 895040876356000000000000000000000000 cm2)""")

  match result_unit:
      case "km2":
        return result / 100000 ** 2
      case "hm2":
        return result / 10000 ** 2
      case "dam2":
        return result / 1000 ** 2
      case "m2":
        return result / 100 ** 2
      case "dm2":
        return result / 10 ** 2
      case "cm2":
        return result
      case "mm2":
        return result * 10 ** 2
      case "µm2":
        return result * 10000 ** 2
      case "square micrometer":
        return result * 10000 ** 2
      case "nm2":
        return result * 10000000 ** 2
      case "square mile":
        return result / 160935 ** 2
      case "yd2":
        return result / 91.44 ** 2
      case "ft2":
        return result / 30.48 ** 2
      case "inch2":
        return result / 2.54 ** 2
      case "square light year":
        return result / 946066000000000000 ** 2
      case _:
        import useful_stuffs.Strings
        import useful_stuffs.Errors
        if type(result_unit) is not str:
          raise useful_stuffs.Errors.NoTypeMatchedError(f"starting_unit requires str, not {useful_stuffs.Strings.return_type(result_unit)}")
        else:
          raise useful_stuffs.Errors.NoValueMatchedError(f"""No area unit available named: {result_unit}
  All area units that are available are:
  1. km2 (1 km2 = 10000000000 cm2)
  2. hm2 (1 hm2 = 100000000 cm2)
  3. dam2 (1 dam = 1000000 cm2)
  4. m2 (1 m = 10000 cm2)
  5. dm2 (1 dm = 100 cm2)
  6. cm2
  7. mm2 (1 mm = 1/100 cm2)
  8. µm2/square micrometer (1 µm = 1/100000000 cm2)
  9. nm2 (1 nm = 1/100000000000000 cm2)
  10. square mile (1 mile = 25900074225 cm2)
  11. yd2 (1 yd = 8361.2736 cm2)
  12. ft2 (1 ft = 929.0304 cm2)
  13. inch2 (1 inch = 6.4516 cm2)
  14. square light year (1 light year = 895040876356000000000000000000000000 cm2)""")
