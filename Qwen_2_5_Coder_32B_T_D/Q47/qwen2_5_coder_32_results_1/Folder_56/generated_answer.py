def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 8, len(s)) + 1):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes