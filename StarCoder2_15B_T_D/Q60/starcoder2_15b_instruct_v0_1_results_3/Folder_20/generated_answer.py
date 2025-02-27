def is_truncatable_prime(num, prime_set):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] == '0':
            return False
        if int(num_str[i:]) not in prime_set:
            return False
        if int(num_str[:len(num_str) - i]) not in prime_set:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    result = []
    for num in nums:
        if is_truncatable_prime(num, prime_set):
            result.append(num)
    result.sort(reverse=True)
    return result