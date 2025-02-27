def sum_of_divisors_in_range(n):

    def divisors(num):
        return [i for i in range(1, num + 1) if num % i == 0]
    div_in_range = [d for d in divisors(n) if 4 <= d <= 5]
    return sum(div_in_range)