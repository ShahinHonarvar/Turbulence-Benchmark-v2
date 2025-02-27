def palindromes_between_indices(s):
    result = set()
    for i in range(4, 7):
        for j in range(i + 1, 8):
            substring = s[i:j].lower()
            if len(substring) >= 4 and substring == substring[::-1]:
                result.add(substring)
    return result