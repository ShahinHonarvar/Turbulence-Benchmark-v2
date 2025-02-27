def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for length in range(18, 74):
        for start in range(15, 95 - length):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result