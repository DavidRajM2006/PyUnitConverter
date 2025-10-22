def convert(value, unit):
    if unit == "g to kg":
        return value / 1000
    elif unit == "kg to g":
        return value * 1000
    elif unit == "lb to kg":
        return value * 0.453592
    elif unit == "kg to lb":
        return value / 0.453592
    elif unit == "g to lb":
        return value * 0.00220462
    elif unit == "lb to g":
        return value / 0.00220462
    else:
        return "Invalid Conversion"