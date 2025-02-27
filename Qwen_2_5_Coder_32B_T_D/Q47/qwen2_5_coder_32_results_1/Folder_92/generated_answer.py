def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for i in range(5):
        for j in range(i + 2, min(i + 5, 6)):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes