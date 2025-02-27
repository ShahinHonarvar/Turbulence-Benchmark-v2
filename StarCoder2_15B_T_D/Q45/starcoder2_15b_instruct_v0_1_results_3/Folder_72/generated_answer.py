def palindromes_between_indices(string):
    palindromes = set()
    letters = [c for c in string.lower() if c.isalpha()]
    for i in range(1, 8):
        for j in range(i + 5, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes