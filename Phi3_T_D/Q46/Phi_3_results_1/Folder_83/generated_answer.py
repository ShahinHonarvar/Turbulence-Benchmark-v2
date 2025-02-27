def gcf_three_nums(positive_ints):
    a, b = (positive_ints[56], positive_ints[54])
    gcd_ab = a if b == 0 else gcd_three_nums_helper(b, a % b)
    return gcd_ab if gcd_ab == 0 else gcd_three_nums_helper(gcd_ab, positive_ints[13])

def gcd_three_nums_helper(a, b):
    return a if b == 0 else gcd_three_nums_helper(b, a % b)