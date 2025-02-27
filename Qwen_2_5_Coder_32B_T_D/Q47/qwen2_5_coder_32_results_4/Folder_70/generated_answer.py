def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:71].lower()
    for length in range(24, 53):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result