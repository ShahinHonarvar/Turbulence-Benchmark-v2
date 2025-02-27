def all_right_truncatable_prime(input_tuple):
    x = input_tuple[4]
    output_list = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            temp = i
            while temp > 0:
                if temp % 2 == 0 or temp % 3 == 0:
                    truncatable = False
                    break
                temp //= 10
            if truncatable:
                output_list.append(i)
    output_list.sort()
    return output_list