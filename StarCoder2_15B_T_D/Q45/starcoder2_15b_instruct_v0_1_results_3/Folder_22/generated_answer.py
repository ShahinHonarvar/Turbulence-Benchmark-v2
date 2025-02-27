def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes