def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i, number in enumerate(numbers):
        if i >= 639 and i <= 975:
            if number > 1:
                for j in range(2, number):
                    if number % j == 0:
                        composite_nums.add(number)
                        break
    return composite_nums