def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[32:80].lower()
    for i in range(35, 42):
        for j in range(len(s) - i):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes