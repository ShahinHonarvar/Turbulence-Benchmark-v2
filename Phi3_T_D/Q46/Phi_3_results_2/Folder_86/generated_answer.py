def gcf_three_nums(lst):
    a = lst[238]
    b = lst[341]
    c = lst[374]

    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)
    a_b_gcf = gcd(a, b)
    return gcd(a_b_gcf, c)