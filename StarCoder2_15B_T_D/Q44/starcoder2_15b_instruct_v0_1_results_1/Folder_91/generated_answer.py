def composite_nums_between_indices(nums):
    result = set()
    for i, num in enumerate(nums):
        if 5 <= i <= 5:
            for j in range(2, num):
                if num % j == 0:
                    result.add(num)
                    break
    return result