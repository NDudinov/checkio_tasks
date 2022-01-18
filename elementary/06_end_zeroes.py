def end_zeros(num: int) -> int:
    t = 0
    i = -1
    s = str(num)
    while (s[i] == '0') and (abs(i) < len(s)):
        t += 1
        i -= 1
        print(t)
    if len(s) == 1 and s[0] == '0':
        t = 1
    return t


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
