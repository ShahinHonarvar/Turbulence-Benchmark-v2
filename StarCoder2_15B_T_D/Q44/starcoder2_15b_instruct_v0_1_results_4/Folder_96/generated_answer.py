def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(60, 201):
        if i in nums:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if not is_prime:
                composite_nums.add(i)
    return composite_nums