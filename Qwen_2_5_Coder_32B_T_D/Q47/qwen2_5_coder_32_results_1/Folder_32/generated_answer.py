def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for l in range(43, 48):
            if i + l <= len(s):
                w = s[i:i + l]
                if all((c.isalpha() for c in w)) and w == w[::-1]:
                    palindromes.add(w)
    return palindromes