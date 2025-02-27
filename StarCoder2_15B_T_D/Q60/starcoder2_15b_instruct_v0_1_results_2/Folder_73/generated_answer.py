def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    result = []
    for i in range(10, x + 1):
        if is_prime(i):
            num = i
            while num >= 10:
                num = int(str(num)[1:])
                if not is_prime(num):
                    break
            else:
                num = i
                while num >= 10:
                    num = int(str(num)[:-1])
                    if not is_prime(num):
                        break
                else:
                    result.append(i)
    result.sort()
    return result