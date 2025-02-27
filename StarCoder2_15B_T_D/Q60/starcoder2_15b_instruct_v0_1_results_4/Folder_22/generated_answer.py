def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[85]

    def is_truncatable(num):
        num_str = str(num)
        if len(num_str) <= 2:
            return num in (2, 3, 5, 7)
        if num_str[0] == '0' or num_str[-1] == '0':
            return False
        return is_truncatable(int(num_str[1:])) and is_truncatable(int(num_str[:-1]))
    result = []
    for num in range(2, x + 1):
        if is_truncatable(num):
            result.append(num)
    result.sort()
    return result