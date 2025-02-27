def isqrt(n):
    return int(n ** 0.5)

def if_perfect_num(lst):
    if 714 < len(lst):
        num = lst[714]
        if num < 1:
            return False
        divisors_sum = 1
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum == num
    return False