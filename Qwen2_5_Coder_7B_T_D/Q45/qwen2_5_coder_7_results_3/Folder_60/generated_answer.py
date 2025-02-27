def palindromes_between_indices(s):
    result = set()
    for i in range(3, 7):
        for j in range(i + 3, 7):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result