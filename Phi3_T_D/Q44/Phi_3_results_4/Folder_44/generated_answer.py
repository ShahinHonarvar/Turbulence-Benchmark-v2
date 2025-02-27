def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(nums_list):
    composite_set = set()
    for i in range(64, 67):
        if not is_prime(nums_list[i]) and nums_list[i] > 1:
            composite_set.add(nums_list[i])
    return composite_set