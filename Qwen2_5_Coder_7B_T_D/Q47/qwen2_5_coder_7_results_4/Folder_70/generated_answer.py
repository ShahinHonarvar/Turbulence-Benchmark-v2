def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(10, 71):
        for j in range(i + 24, min(j + 53, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result