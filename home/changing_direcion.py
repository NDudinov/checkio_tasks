def changing_direction(elements: list[int]) -> int:
    result = 0
    direction = ""
    for i in range(1, len(elements)):
        if elements[i] > elements[i-1]:
            direction = "up"
            break
        elif elements[i] < elements[i-1]:
            direction = "down"
            break
        else:
            direction = "same"
    for i in range(1, len(elements)):
        if elements[i] < elements[i-1] and direction == "up":
            direction = "down"
            result += 1
        elif elements[i] > elements[i-1] and direction == "down":
            direction = "up"
            result += 1
        else:
            pass
    return result


# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
