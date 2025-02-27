def gcf_two_nums(lst):
    a = lst[278]
    b = lst[811]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(a, b)