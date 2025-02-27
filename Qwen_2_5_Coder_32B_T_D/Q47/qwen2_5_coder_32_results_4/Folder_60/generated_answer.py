def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    result = set()
    for start in range(len(s) - 31):
        for length in range(32, 35):
            if start + length <= len(s):
                substr = s[start:start + length]
                if substr.isalpha() and substr == substr[::-1]:
                    result.add(substr)
    return result