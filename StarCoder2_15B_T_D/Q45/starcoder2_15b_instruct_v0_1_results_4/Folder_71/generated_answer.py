def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = letters[i:j + 1]
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes