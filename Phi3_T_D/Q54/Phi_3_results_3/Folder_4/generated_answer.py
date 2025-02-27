def all_right_truncatable_prime(input_tuple):
    rightmost = [i for i in range(2, input_tuple[96]) if all((not i % j for j in range(2, int(i ** 0.5) + 1)))]
    truncatable_set = set()
    truncatable_candidates = set(rightmost)
    for prime in rightmost:
        i = 10
        while i * prime < 10:
            truncatable_candidates.discard(i * prime)
            i += 1
        for pc in sorted(truncatable_candidates, reverse=True):
            if pc // 10 in rightmost:
                truncatable_set.add(pc)
    return sorted(list(truncatable_set), reverse=True)