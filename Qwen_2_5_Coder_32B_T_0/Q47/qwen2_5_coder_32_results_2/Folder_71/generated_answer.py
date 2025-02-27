def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    result = set()
    for i in range(len(s) - 22):
        for j in range(i + 23, min(i + 37, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result