def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    letters_lower = [c.lower() for c in letters]
    palindromes = set()
    for i in range(3, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = ''.join(letters_lower[i:j + 1])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes