def composite_nums_between_indices(nums):
    is_composite = [False] * (max(nums) + 1)
    for i in range(2, len(is_composite)):
        if is_composite[i]:
            continue
        for j in range(i * 2, len(is_composite), i):
            is_composite[j] = True
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite[num] and 60 <= i <= 200:
            composite_nums.add(num)
    return composite_nums