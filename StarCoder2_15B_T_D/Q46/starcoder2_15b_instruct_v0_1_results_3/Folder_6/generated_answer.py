def gcf_three_nums(numbers):
    a = numbers[93]
    b = numbers[94]
    c = numbers[57]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    gcf = a
    while gcf != c:
        if gcf > c:
            gcf -= c
        else:
            c -= gcf
    return gcf