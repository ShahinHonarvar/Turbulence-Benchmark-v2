def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    if len(letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 6, len(s) + 1):
            word = s[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes