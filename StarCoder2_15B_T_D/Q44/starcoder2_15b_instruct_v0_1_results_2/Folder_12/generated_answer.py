def composite_nums_between_indices(nums):
    result = set()
    for i, num in enumerate(nums):
        if i < 51 or i > 86:
            continue
        is_composite = False
        for j in range(2, num):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            result.add(num)
    return result