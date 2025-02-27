def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[125]
    left_truncatable, right_truncatable = (set(), set())
    for num in range(11, max_val + 1):
        if is_prime(num):
            s = str(num)
            left_checked = True
            right_checked = True
            for i in range(1, len(s)):
                if not is_prime(int(s[i:])):
                    left_checked = False
                if not is_prime(int(s[:-i])):
                    right_checked = False
            if left_checked and right_checked:
                left_truncatable.add(num)
                right_truncatable.add(num)
    result = list(left_truncatable.intersection(right_truncatable))
    result.sort(reverse=True)
    return result