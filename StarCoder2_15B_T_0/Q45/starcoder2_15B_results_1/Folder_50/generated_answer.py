def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 4):
        for j in range(i + 5, len(letters)):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes