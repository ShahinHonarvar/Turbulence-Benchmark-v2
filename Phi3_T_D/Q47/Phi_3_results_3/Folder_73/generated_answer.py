def palindromes_of_specific_lengths(s):
    start = 20
    end = 61
    result_set = set()
    for length in range(22, 34):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result_set.add(substring)
    return result_set