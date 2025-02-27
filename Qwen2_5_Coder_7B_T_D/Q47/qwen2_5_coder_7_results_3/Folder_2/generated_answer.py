def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:60].lower()
    for length in range(18, 37):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result