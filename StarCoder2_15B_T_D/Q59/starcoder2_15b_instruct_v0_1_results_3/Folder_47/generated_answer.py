def all_left_truncatable_prime(x):

    def is_truncatable_prime(number, prime_list):
        if number not in prime_list:
            return False
        if number < 10:
            return True
        return is_truncatable_prime(int(str(number)[1:]), prime_list)
    prime_list = [i for i in range(2, x) if all((i % j != 0 for j in range(2, i)))]
    return sorted([num for num in prime_list if is_truncatable_prime(num, prime_list)])