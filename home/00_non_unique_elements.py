def checkio(data: list) -> list:
    non_unique_data = []
    for e in data:
        entrance_count = data.count(e)
        if entrance_count != 1:
            non_unique_data.append(e)
    return non_unique_data


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
