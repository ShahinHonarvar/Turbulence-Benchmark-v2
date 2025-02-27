def sum_of_divisors_in_range(n):

    def find_divisors(num):
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    all_divisors = find_divisors(n)
    sum_in_range = sum((div for div in all_divisors if 70 <= div <= 93))
    return sum_in_range