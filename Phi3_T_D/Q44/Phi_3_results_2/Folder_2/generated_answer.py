def composites_helper(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {lst[i] for i in range(35, 50) if composites_helper(lst[i])}