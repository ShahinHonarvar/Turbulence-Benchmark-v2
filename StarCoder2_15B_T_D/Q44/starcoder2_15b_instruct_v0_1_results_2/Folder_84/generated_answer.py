def is_composite(num):
    """
    Returns True if the given number is composite, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 30 <= i <= 48:
            composite_nums.add(num)
    return composite_nums