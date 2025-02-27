def palindromes_between_indices(string):
    letters = [char for char in string[8:10].lower() if char.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]) + ''.join(letters[j:i:-1]))
    return palindromes