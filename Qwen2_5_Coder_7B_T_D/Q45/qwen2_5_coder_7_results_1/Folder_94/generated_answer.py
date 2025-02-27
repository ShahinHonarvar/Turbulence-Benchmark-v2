def palindromes_between_indices(s):
    result = set()
    for i in range(3, 5):
        for j in range(i + 3, 6):
            substring = s[i:j + 1].lower()
            if len(substring) >= 3 and substring == substring[::-1]:
                result.add(substring)
    return result