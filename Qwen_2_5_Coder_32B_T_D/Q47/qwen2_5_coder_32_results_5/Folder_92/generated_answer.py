def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for i in range(5):
        for j in range(i + 3, min(5, i + 5)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes