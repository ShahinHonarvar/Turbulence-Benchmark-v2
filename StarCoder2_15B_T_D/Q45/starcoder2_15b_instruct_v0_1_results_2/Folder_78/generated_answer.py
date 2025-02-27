def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1][::-1]
            if len(palindrome) >= 3 and palindrome == letters[i:j + 1]:
                palindromes.add(''.join(palindrome))
    return palindromes