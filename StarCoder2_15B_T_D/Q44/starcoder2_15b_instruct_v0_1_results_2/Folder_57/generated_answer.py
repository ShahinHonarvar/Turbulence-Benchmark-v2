def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i, num in enumerate(list_of_nums):
        if i >= 25 and i <= 59:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums