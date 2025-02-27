def palindromes_of_specific_lengths(s):
    s = s[35:89].lower()
    palindromes = set()
    for i in range(len(s) - 23):
        for l in range(24, 34):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes