def replace(arr, index, value):
    if 0 <= index < len(arr):
        arr.pop(index)
        arr.insert(index, value)
        print(arr)
    else:
        raise IndexError("Replace Function: Index specified out of range,", str(index), "is higher than", str(len(arr)))

def time_format(dur):
    seconds = dur
    minutes = 0
    hours = 0
    days = 0

    while True:
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        elif minutes >= 60:
            hours += 1
            minutes -= 60
        elif hours >= 24:
            days += 1
            hours -= 24
        else:
            break

    seconds_formatted = "0" + str(seconds) if len(str(seconds)) == 1 else seconds
    minutes_formatted = "0" + str(minutes) if len(str(minutes)) == 1 else minutes
    hours_formatted = "0" + str(hours) if len(str(hours)) == 1 else hours

    time_formatted = str(days) + ":" + str(hours_formatted) + ":" + str(minutes_formatted) + ":" + str(seconds_formatted)

    return time_formatted

def countdown(duration, decrement):
    import time

    if isinstance(duration, int) and isinstance(decrement, int):
        for remaining in range(duration, 0, -decrement):
            if duration - decrement > 0:
                tleft = time_format(remaining)
                print(tleft)
                time.sleep(decrement)
        print("Countdown Complete")
    else:
        raise ValueError("The given time or decrease of time must both be integers or floats")

countdown(100, 1)


























