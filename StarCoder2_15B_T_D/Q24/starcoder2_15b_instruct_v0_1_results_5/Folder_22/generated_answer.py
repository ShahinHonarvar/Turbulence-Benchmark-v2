def sum_of_divisors_in_range(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    filtered_divisors = [divisor for divisor in divisors if 4 <= divisor <= 7]
    sum_of_filtered_divisors = sum(filtered_divisors)
    return sum_of_filtered_divisors