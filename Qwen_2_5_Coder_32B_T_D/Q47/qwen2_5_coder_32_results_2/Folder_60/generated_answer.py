def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    result = set()
    for length in range(32, 35):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result