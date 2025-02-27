def palindromes_of_specific_lengths(s):
    s = s[100:201].lower()
    result = set()
    for i in range(len(s) - 4):
        for j in range(i + 5, min(i + 11, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result