def palindromes_between_indices(s):
    letters = s[7:10].lower()
    if len(letters) < 4:
        return set()
    letters = ''.join(sorted(letters))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes