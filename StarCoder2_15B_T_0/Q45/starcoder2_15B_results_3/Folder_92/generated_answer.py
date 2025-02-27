def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 3):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes