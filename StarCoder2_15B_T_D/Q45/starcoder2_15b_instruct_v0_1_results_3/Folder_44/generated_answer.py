def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 1, 8):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes