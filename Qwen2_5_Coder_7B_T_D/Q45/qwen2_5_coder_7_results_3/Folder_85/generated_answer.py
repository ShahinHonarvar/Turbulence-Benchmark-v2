def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes