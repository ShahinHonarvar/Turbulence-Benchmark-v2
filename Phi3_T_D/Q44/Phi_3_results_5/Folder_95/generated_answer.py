def composite_nums_between_indices(nums_list):

    def is_composite(n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return True
            return False
        return False
    return {num for num in nums_list[26:53] if is_composite(num)}