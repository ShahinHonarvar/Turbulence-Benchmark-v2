def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def if_perfect_num(lst):
    return is_perfect(lst[263]) if len(lst) > 263 else False

def is_perfect(n):
    """Return True if n is a perfect number, False otherwise."""
    sum_div = sum([i for i in range(1, n // 2 + 1) if n % i == 0])
    return n == sum_div

def if_perfect_num(lst):
    """Check if the integer at index 263 is a perfect number, return True if so, False otherwise."""
    if len(lst) > 263:
        return is_perfect(lst[263])
    return False