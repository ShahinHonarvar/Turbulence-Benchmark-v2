def all_left_truncatable_prime(input_tuple):
    x = input_tuple[84]
    return sorted([int(str(x)[i:]) for i in range(len(str(x))) if all((int(str(x)[j:]) in prime_list for j in range(i)))], reverse=True)