def palindromes_between_indices(string):
    letters = [letter for letter in string[6:10].lower() if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]))
    return palindromes