def gcf_three_nums(numbers):
    a, b, c = (numbers[9], numbers[6], numbers[2])
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