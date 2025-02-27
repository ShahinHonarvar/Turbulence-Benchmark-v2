import math

def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[0:i])):
                return False
        return True
    x = tup[36]
    prime_list = [i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    prime_list.sort(reverse=True)
    return prime_list