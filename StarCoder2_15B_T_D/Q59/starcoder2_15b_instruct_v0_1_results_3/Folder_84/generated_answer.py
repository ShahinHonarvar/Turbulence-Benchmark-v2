def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[630]
    output = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            left_truncatable = True
            temp = i
            while temp > 0:
                if temp % 10 == 0:
                    left_truncatable = False
                    break
                temp //= 10
            if left_truncatable:
                output.append(i)
    output.sort(reverse=True)
    return output