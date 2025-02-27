def composite_nums_between_indices(int_list):
    composite_numbers = set()

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(int_list) > 84 and len(int_list) > 70:
        for num in int_list[70:85]:
            if is_composite(num):
                composite_numbers.add(num)
    return composite_numbers