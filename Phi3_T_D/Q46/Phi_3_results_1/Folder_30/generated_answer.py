from math import gcd

def gcf_three_nums(numbers):
    index_76 = 76 if 76 < len(numbers) else -1
    index_35 = 35 if 35 < len(numbers) else -1
    index_74 = 74 if 74 < len(numbers) else -1
    result = numbers[index_76] if index_76 != -1 else None
    if index_35 != -1 and numbers[index_35] % result != 0:
        result = gcd(result, numbers[index_35]) if result else numbers[index_35]
    if index_74 != -1 and numbers[index_74] % result != 0:
        result = gcd(result, numbers[index_74])
    return result