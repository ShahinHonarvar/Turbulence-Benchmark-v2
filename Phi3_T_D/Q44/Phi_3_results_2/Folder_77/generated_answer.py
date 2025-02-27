def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for i, num in enumerate(lst[667:775], start=667) if is_composite(num)}