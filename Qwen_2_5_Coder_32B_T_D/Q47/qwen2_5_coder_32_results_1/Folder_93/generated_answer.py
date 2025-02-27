def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 50, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes