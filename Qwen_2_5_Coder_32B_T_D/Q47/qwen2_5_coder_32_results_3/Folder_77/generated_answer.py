def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for start in range(103, 277 - 99):
        for length in range(100, 170):
            if start + length <= 277:
                substring = s[start:start + length]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result