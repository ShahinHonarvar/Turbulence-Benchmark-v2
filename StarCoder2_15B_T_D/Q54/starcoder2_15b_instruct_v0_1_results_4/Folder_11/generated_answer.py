def all_right_truncatable_prime(args):
    x = args[0]
    if x < 2:
        return []
    prime = [True] * x
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x, i):
                prime[j] = False
    truncatable_prime = []
    for i in range(10, x):
        if prime[i]:
            right_truncatable = True
            for j in range(len(str(i)) - 1):
                if not prime[int(str(i)[j:])]:
                    right_truncatable = False
                    break
            if right_truncatable:
                truncatable_prime.append(i)
    return sorted(truncatable_prime)