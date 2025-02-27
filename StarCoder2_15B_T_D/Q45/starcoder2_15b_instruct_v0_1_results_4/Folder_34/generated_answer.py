def palindromes_between_indices(string):
    """
    """
    letters = [c for c in string[5:8].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]))
    return palindromes