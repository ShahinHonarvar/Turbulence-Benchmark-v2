def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for length in range(29, 63):
        for start in range(11, 98 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result