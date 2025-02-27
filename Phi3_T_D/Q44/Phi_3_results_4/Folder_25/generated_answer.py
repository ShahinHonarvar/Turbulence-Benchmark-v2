def composite_nums_between_indices(int_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    composite_set = set()
    for i in range(75, 95):
        if not is_prime(int_list[i]) and int_list[i] > 1:
            composite_set.add(int_list[i])
    return composite_set