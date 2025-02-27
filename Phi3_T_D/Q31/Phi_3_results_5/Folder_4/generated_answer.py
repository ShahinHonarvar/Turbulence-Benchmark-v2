def is_perfect_num(num_list):
    if len(num_list) < 16:
        return False

    def sum_of_divisors(n):
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors)
    return sum_of_divisors(num_list[15]) == num_list[15]