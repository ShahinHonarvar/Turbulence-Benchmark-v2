def palindromes_between_indices(s):
    letters = s[6:10]
    letters = ''.join(filter(str.isalpha, letters.lower()))
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes