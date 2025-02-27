def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    result = set()
    for start in range(len(s) - 34):
        for length in range(35, 42):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result