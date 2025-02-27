def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 6):
        for j in range(i + 6, len(letters)):
            palindrome = letters[i:j + 1]
            if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes