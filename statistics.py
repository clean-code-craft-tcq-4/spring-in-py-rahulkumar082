import math

def calculateStats(numbers):
    if (len(numbers) != 0):
        average = sum(numbers) / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
    else:
        average = math.nan
        maximum = math.nan
        minimum = math.nan
    return {"avg": average, "max": maximum, "min": minimum}
