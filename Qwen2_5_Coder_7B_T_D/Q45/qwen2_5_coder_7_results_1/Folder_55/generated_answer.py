def palindromes_between_indices(s):
    result = set()
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result