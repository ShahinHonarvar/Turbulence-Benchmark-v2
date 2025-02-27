def palindromes_between_indices(s):
    result = set()
    letters = s[:6].lower()
    n = len(letters)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 6:
                result.add(substring)
    return result