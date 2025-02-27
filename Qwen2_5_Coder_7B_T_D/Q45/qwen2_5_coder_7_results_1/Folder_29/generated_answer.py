def palindromes_between_indices(s):
    substring = s[2:10].lower()
    letters = list(substring)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            sub = ''.join(letters[i:j + 1])
            if sub == sub[::-1] and len(sub) >= 6:
                palindromes.add(sub)
    return palindromes