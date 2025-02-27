def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) > 663 and len(lst) > 224:
        num1 = lst[224]
        num2 = lst[663]
        return gcd(num1, num2)
    else:
        raise ValueError('List must have at least 664 elements')