def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s if c.isalpha()]
    n = len(letters)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            palindrome = ''.join(letters[i:j + 1]).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes