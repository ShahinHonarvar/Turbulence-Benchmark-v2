def palindromes_between_indices(s):
    result = set()
    letters = s[:8].lower()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result