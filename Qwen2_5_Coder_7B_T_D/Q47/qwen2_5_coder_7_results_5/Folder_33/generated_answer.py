def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(103, 159):
        for start in range(130, 296 - length):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result