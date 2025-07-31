def check_limit(value, low, high):
    return low <= value <= high

def battery_is_ok(temperature, soc, charge_rate):
    limits = [
        (temperature, 0, 45),
        (soc, 20, 80),
        (charge_rate, 0, 0.8)
    ]
    return all(check_limit(value, low, high) for value, low, high in limits)

if __name__ == '__main__':
    assert(battery_is_ok(4, 21, 1.0) is False)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(25, 70, 0.7) is True)
