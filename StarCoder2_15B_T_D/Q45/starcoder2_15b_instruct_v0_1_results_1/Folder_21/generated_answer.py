def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    n = len(letters)
    palindromes = set()
    for i in range(n - 6):
        for j in range(i + 6, n):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes