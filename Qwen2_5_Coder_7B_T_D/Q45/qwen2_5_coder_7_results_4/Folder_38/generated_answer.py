def palindromes_between_indices(s):
    subset = s[3:9].lower()
    letters = [c for c in subset if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters) + 1):
            word = ''.join(letters[i:j])
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes