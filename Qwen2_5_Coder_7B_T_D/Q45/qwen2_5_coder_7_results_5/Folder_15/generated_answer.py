def palindromes_between_indices(s):
    letters = s[1:3].lower()
    result = set()
    n = len(letters)
    for i in range(n):
        for j in range(i, n):
            substring = letters[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                result.add(substring)
    return result