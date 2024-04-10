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
    # We initialize our variables. Here, seconds is equal to the dur variable, which, let's say is 420 (I'm so funny.... right?)
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
    # After this point, seconds should be LESS than 60, and then transferred the excess to minutes, and then minutes to hours, ending with hours to days. Days can be infinite by the way. When we continue our last example, it will be 0 seconds, 7 minutes
    seconds_formatted = "0" + str(seconds) if len(str(seconds)) == 1 else seconds
    minutes_formatted = "0" + str(minutes) if len(str(minutes)) == 1 else minutes
    hours_formatted = "0" + str(hours) if len(str(hours)) == 1 else hours
    # This part formats all the variables, for example, let's say that minutes is still 7, this code will turn it into "07", but if it's already double digit, then it will be left alone
    time_formatted = str(days) + ":" + str(hours_formatted) + ":" + str(minutes_formatted) + ":" + str(seconds_formatted)
    # Now we smash together all the variables, for example: 5 seconds + 10 minutes + 7 hours + 3 days will show as 3:07:10:05!
    return time_formatted
    # This is here the value of the time in formatted state will be returned
def countdown(duration, decrement):
    import time
    # Initialize the time module so that we have a genuine countdown
    if isinstance(duration, int) and isinstance(decrement, int): # Trust me, if I use any other class, stuff gets wild. By wild I mean, it doesn't work at all
        for remaining in range(duration, 0, -decrement):
            if duration - decrement > 0: # It checks if decrement is less than remaining time.
                tleft = time_format(remaining) # This is where the formatted version of the time comes into play
                print(tleft)
                time.sleep(decrement)
            else:
                time.sleep(duration) # If it's not, it will simply wait the little time left. We don't want any negative numbers. That'll break it!
                
        print("Countdown Complete")
    else:
        raise ValueError("The given time or decrease of time must both be integers") # Don't you dare...

countdown(100, 1) # Test for yourself


























