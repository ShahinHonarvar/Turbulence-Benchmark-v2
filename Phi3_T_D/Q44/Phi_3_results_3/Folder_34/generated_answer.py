def composite_nums_between_indices(arr):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set(filter(is_composite, arr[70:201]))