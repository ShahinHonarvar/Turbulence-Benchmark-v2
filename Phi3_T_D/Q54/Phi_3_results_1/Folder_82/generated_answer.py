def all_right_truncatable_prime(nums):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def generate_truncatable_sequence(number, index):
        if index == 0:
            return [number] if is_prime(number) else []
        sequences = [generate_truncatable_sequence(number // 10, index - 1)]
        if is_prime(number):
            sequences.append([number])
        return [seq if is_prime(number) else [] for seq in sequences for number in seq]
    x = nums[69]
    truncatable_primes = set()
    for number in range(7, x):
        sequences = generate_truncatable_sequence(number, len(str(number)))
        for seq in sequences:
            truncatable_primes.add(int(''.join(map(str, seq))))
    if x >= 7:
        truncatable_primes.discard(7)
    return sorted(truncatable_primes, reverse=True)