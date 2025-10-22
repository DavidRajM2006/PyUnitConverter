def convert(value, unit):
    if unit == "C to F":
        return (value * 9/5) + 32
    elif unit == "F to C":
        return (value - 32) * 5/9
    elif unit == "C to K":
        return value + 273.15
    elif unit == "K to C":
        return value - 273.15
    elif unit == "F to K":
        return (value - 32) * 5/9 + 273.15
    elif unit == "K to F":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid Conversion"