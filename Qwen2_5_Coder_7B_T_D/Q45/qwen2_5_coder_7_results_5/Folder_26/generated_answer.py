def palindromes_between_indices(s):
    letters = s[4:7]
    letters = letters.lower()
    letters = list(letters)
    letters.sort()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes