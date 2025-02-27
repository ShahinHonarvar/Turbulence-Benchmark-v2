def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 2, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]))
    return {p for p in palindromes if len(p) >= 4 and p == p[::-1]}