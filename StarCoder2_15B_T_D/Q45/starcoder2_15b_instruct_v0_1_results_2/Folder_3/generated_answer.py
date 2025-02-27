def palindromes_between_indices(text):
    letters = sorted(text[7:10].lower())
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                palindrome = letters[i] + letters[j] + letters[k]
                palindromes.add(palindrome)
                reversed_palindrome = palindrome[::-1]
                palindromes.add(reversed_palindrome)
    return palindromes