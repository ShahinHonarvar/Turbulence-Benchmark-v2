def palindromes_between_indices(s):
    result = set()
    for i in range(len(s) - 2):
        if 8 <= i <= 9 and s[i].isalpha():
            for j in range(i + 2, len(s) + 1):
                substring = s[i:j].lower()
                if substring == substring[::-1]:
                    result.add(substring)
    return result