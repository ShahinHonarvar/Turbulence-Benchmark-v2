def palindromes_of_specific_lengths(s):
    result = set()
    s = s[31:75].lower()
    for i in range(23, 40):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                result.add(substring)
    return result