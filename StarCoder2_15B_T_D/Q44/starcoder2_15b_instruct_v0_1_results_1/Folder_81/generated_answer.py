def composite_nums_between_indices(numbers):
    """
    Returns the set of all composite numbers in the given list `numbers` that are between
    index 20 and index 200, both inclusive. If no composite number exists in the specified
    range, returns an empty set.
    """
    composite_nums = set()
    is_prime = [True] * (max(numbers) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(numbers) + 1, i):
                is_prime[j] = False
    for i, num in enumerate(numbers):
        if not is_prime[num] and 20 <= i <= 200:
            composite_nums.add(num)
    return composite_nums