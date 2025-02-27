def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    target = set()
    for i in range(333, 369):
        if is_composite(lst[i]):
            target.add(lst[i])
    return target