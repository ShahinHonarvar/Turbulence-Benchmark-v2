def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(4, min(len(letters), 9)):
        for j in range(len(letters) - i + 1):
            palindrome = letters[j:j + i]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes