def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = list(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            word = ''.join(letters[i:j])
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes