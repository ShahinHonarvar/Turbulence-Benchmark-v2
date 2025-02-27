def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    palindromes = set()
    for start in range(len(s) - 36):
        for length in range(37, 61):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes