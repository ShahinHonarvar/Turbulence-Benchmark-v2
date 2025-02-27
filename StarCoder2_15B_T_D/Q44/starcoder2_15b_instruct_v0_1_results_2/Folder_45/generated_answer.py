def composite_nums_between_indices(nums):
    """
    This function takes a list of positive integers as an argument
    and returns the set of all composite numbers between indices 40 and 200,
    both inclusive. If no composite number exists in the specified range,
    the function returns an empty set.
    """
    composite_nums = set()
    for i, num in enumerate(nums):
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    if 40 <= i <= 200:
                        composite_nums.add(num)
                    break
    return composite_nums