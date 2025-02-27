def composite_nums_between_indices(nums):
    composite = set()
    for i, num in enumerate(nums):
        if i >= 686 and i <= 987:
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite.add(num)
                        break
    return composite