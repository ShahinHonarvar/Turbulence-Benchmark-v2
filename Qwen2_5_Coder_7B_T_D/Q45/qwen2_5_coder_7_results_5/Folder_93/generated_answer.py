def palindromes_between_indices(s):
    letters = s[2:8]
    letters = letters.lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    result = set()
    for i in range(n - 5):
        for j in range(i + 5, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result