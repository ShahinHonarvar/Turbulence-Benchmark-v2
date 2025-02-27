def palindromes_between_indices(s):
    result = set()
    for i in range(1, 6):
        for j in range(i + 1, 6):
            substring = s[i:j].lower()
            if len(substring) >= 2 and substring == substring[::-1]:
                result.add(substring)
    return result