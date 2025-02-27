def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 1, 9):
            palindrome = letters[i:j] + letters[i:j][::-1]
            palindromes.add(''.join(palindrome).lower())
    return {p for p in palindromes if len(p) >= 6 and p == p[::-1]}