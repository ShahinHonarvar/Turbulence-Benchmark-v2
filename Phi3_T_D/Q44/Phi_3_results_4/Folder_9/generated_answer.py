def composite_nums_between_indices(int_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    composites = {x for x in int_list[80:201] if not is_prime(x) and x > 1}
    return composites