# def nearest_value1(values: set, one: int) -> int:
#     if one in values:
#         return one
#     else:
#         for n in values:
#             t = n
#             if n - one >
#     return

def nearest_value(values: set, one: int) -> int:
    return sorted((abs(one - v), v) for v in values)[0][1]


def nearest_value2(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
