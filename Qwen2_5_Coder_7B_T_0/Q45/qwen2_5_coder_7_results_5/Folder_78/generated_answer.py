def palindromes_between_indices(s):
    letters = s[6:9].lower()
    letters = ''.join(filter(str.isalpha, letters))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes