def all_left_truncatable_prime(arg):
    x = arg[96]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % i != 0:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result