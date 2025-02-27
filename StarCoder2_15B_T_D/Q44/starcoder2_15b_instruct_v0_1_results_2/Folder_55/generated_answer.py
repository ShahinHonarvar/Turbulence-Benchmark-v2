def is_composite(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if is_composite(num) and 10 <= i <= 100:
            composite_nums.add(num)
    return composite_nums