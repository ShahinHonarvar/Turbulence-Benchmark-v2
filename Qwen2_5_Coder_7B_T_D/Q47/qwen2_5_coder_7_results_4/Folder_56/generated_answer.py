def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(1, 10):
        for j in range(i, min(i + 7, 10)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result