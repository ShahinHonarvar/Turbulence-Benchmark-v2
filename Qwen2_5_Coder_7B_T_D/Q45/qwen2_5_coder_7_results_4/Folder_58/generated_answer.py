def palindromes_between_indices(s):
    letters = s[:7].lower()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 6:
                result.add(substring)
    return result