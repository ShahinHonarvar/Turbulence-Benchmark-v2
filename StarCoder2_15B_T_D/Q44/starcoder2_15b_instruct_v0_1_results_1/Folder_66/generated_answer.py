def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    composite_nums = set()
    for i, num in enumerate(lst):
        if is_composite(num) and 62 <= i <= 63:
            composite_nums.add(num)
    return composite_nums