def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(12, 221):
        for start in range(12, len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result