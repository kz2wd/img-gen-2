def check_presence(value, list_to_check):
    presence = False
    for element in list_to_check:
        if value == element:
            presence = True

    return presence


def divide_to_superior(value, divisor):
    value = int(value / divisor) + 1
    return value


def cycle(value, value_max):
    while value > value_max:
        value -= value_max
    return value


def better_round(value):
    if value - int(value) > 0.5:
        return int(value) + 1
    else:
        return int(value)
