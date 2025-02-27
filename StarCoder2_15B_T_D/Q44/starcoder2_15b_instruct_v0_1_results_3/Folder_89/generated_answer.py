def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    output = set()
    for i, num in enumerate(lst):
        if is_composite(num) and 36 <= i <= 46:
            output.add(num)
    return output