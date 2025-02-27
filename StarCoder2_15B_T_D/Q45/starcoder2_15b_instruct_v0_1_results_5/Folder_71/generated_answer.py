def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 3):
        for j in range(i + 3, len(letters)):
            word = ''.join(letters[i:j + 1])
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes