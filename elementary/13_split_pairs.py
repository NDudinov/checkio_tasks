def split_pairs(a):
    l1 = list(a)
    x = len(l1)
    l2 = []
    for i in range(x):
        if not i % 2 == 0:
            l2.append(l1[i - 1] + l1[i])
    if not x == 0:
        if i % 2 == 0:
            l2.append(l1[i] + "_")
    return l2


def split_pairs2(a):
    if len(a) % 2 != 0:
        a += '_'
    return [a[i:i + 2] for i in range(0, len(a), 2)]


import itertools, operator


def split_pairs3(a):
    it = itertools.chain(a, '_')
    return map(operator.add, it, it)


def split_pairs4(a):
    return [ch1+ch2 for ch1, ch2 in zip(a[::2], a[1::2]+'_')]


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
