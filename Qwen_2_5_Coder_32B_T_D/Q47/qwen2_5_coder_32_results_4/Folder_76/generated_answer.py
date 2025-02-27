def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    palindromes = set()
    for start in range(len(s) - 153):
        for length in range(154, 183):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes