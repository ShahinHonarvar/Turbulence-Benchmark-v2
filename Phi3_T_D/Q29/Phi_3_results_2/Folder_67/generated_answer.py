def gcf_two_nums(arr):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(arr) < max(64, 28):
        raise ValueError('List must contain at least 68 elements')
    return gcd(arr[64], arr[28])