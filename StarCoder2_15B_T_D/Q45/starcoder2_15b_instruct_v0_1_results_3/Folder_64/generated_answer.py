def palindromes_between_indices(string):
    letters = sorted([letter for letter in string[4:10].lower() if letter.isalpha()])
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters)):
            palindrome = letters[i:j + 1]
            if len(palindrome) >= 5:
                palindromes.add(''.join(palindrome))
    return palindromes