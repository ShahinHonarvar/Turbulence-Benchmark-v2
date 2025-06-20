def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def composite_nums_between_indices(lst):
    return {x for x in lst[50:201] if not is_prime(x)}