def palindromes_between_indices(s):
    letters = s[2:10].lower()
    n = len(letters)
    result = set()
    for i in range(n - 6):
        for j in range(i + 6, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result