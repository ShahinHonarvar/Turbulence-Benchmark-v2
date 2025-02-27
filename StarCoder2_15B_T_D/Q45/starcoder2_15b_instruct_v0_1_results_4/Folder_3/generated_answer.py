def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s if ch.isalpha()]
    palindromes = set()
    for i in range(7, min(9, len(letters)) + 1):
        for j in range(i + 1, min(9, len(letters)) + 1):
            palindrome = letters[i:j][::-1] + letters[i:j]
            palindromes.add(''.join(palindrome))
    return palindromes