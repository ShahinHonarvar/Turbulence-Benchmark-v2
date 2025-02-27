def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes