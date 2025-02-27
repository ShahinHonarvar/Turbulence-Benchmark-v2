def palindromes_between_indices(string):
    letters = [c for c in string[4:8].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = letters[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes