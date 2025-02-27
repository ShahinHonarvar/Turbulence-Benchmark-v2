def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindromes = set()
    for i in range(len(s) - 19):
        for j in range(i + 20, min(i + 22, len(s)) + 1):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes