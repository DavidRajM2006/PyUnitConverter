def convert(value, unit):
    if unit == "cm to m":
        return value / 100
    elif unit == "m to cm":
        return value * 100
    elif unit == "km to m":
        return value * 1000
    elif unit == "m to km":
        return value / 1000
    elif unit == "inch to cm":
        return value * 2.54
    elif unit == "cm to inch":
        return value / 2.54
    elif unit == "feet to m":
        return value * 0.3048
    elif unit == "m to feet":
        return value / 0.3048
    else:
        return "Invalid Conversion"