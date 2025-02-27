def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 6):
        for j in range(i + 6, len(letters)):
            word = ''.join(letters[i:j + 1])
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes