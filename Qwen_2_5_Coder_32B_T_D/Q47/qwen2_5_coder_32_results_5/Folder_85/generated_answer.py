def palindromes_of_specific_lengths(s):
    s = s[29:99].lower()
    palindromes = set()
    for i in range(len(s) - 5):
        for j in range(i + 5, min(i + 10, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes