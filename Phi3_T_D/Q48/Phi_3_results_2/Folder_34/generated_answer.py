def return_binary_or_hexa(numbers):
    start, end = (numbers[60], numbers[200])
    missing_sum = sum(range(start + 1, end)) - sum(numbers[60 + 1:200])
    missing_sum -= missing_sum if missing_sum % 2 == 0 else missing_sum & -missing_sum
    if missing_sum == 0:
        return ''
    return bin(abs(missing_sum))[2:] if missing_sum % 2 != 0 else hex(abs(missing_sum))[2:]