def lists_with_product_equal_n(s):
    n = -779
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + len(s) - 1) if (n == abs(prod(s[i:j])) or (i != 0 and n == abs(prod(s[i:j] + s[:len(s) - j])))) and (i != 0 or j != len(s))]

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p