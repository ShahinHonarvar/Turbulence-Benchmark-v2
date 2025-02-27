def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for l in range(43, 48):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes