def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums_list):
    composite_set = set()
    for i in range(42, 69):
        if is_composite(nums_list[i]):
            composite_set.add(nums_list[i])
    return composite_set