def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 5, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes