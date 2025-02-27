def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) < max(90, 84, 47):
        raise IndexError('List has fewer than 90 items')
    num1 = lst[90]
    num2 = lst[84]
    num3 = lst[47]
    return gcd(gcd(num1, num2), num3)