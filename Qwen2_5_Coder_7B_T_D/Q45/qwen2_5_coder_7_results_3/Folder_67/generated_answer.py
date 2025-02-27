def palindromes_between_indices(s):
    result = set()
    for i in range(2, len(s) - 3):
        for j in range(i + 4, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result