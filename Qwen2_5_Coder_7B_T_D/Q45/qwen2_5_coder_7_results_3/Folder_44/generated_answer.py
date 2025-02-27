def palindromes_between_indices(s):
    letters = s[2:8]
    letters = letters.lower()
    letters = ''.join(filter(str.isalpha, letters))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes