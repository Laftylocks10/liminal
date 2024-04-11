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
                print("ime left:", tleft)
                time.sleep(decrement)
            else:
                time.sleep(duration) # If it's not, it will simply wait the little time left. We don't want any negative numbers. That'll break it!
                
        print("Countdown Complete")
    else:
        raise ValueError("The given time or decrease of time must both be integers") # Don't you dare...

countdown(100, 1) # Test for yourself

# The following is random functions I made within this. They're not really the main thing I want you to look at so, uh. Enjoy

def replace(arr, index, value):
    if 0 <= index < len(arr):
        arr.pop(index)
        arr.insert(index, value)
        print(arr)
    else:
        raise IndexError("Replace Function: Index specified out of range,", str(index), "is higher than", str(len(arr)))

def removeclass(arr, classval):
    holder = []
    for _index, elementval in enumerate(arr):
        if not isinstance(elementval, classval):
            holder.append(elementval)
    print("Old Version of array:", arr)
    arr = holder
    print("Updated Version of array:", arr)
    
def removereps(arr):
    holder = []
    for _index, elementval in enumerate(arr):
        if elementval not in holder:
            holder.append(elementval)
    print("Array with repetitions:", arr)
    arr = holder
    print("New array without repetitions:", arr)

def shuffle(arr):
    import random
    holder = []
    chosindices = []
    
    for index in range(len(arr)):
        while True:
            randomindex = random.randint(0,len(arr)-1)
            if randomindex not in chosindices:
                chosindices.append(randomindex)
                break
        holder.append(arr[randomindex])
    arr = holder
    print("Shuffled Version of array:", arr)
        
def removeoccurs(arr, occurance):
    holder = []
    for index, elementval in enumerate(arr):
        if elementval != occurance:
            holder.append(elementval)
    print("New array without occurance:", occurance)
    print(holder)

def removerandom(arr, amount):
    for counter in range(amount):
        possible = len(arr) - 1
        randindex = random.randint(0, possible)
        randval = arr[randindex]
        del arr[randindex]
        print("Removed index", randindex, "or value", randval)
        
def removevowels(val): # Currently only supports arrays and strings. It uses return, so you must define values
    holder = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", U"]
    if isinstance(val, str):
        replaceval = ""
        for _indexz, character in enumerate(elementval):
            if character not in vowels:
                replaceval.append(character)
        return replaceval
    elif isinstance(val, list):
        for _indexy, elementval in enumerate(val):
            if isinstance(elementval, str):
                replaceval = ""
                for _indexz, character in enumerate(elementval):
                    if character not in vowels:
                        replaceval.append(character)
                holder[indexy] = replaceval
        return holder
            else:
                holder.append(elementval)
    else:
        raise ValueError("Only strings and arrays are supported")
