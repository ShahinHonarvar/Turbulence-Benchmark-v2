def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[42]
    now_ans = []

    def add_possible_truncatable_prime(number, idx=len(str(number))):
        if is_prime(number):
            now_ans.append(number)
        if idx > 1 and number != 0:
            add_possible_truncatable_prime(number // 10, idx - 1)
    for i in range(2, x):
        if now_ans.count(i) == 0 and is_prime(i):
            add_possible_truncatable_prime(i)
    return sorted(list(set(now_ans)))