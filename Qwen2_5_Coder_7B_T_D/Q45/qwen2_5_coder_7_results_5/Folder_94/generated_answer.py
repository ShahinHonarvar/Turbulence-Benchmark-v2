def palindromes_between_indices(s):
    result = set()
    for i in range(3, 5):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1] and len(substring) >= 3:
                result.add(substring)
    return result