def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    result = set()
    for i in range(10, 51):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                result.add(substring)
    return result