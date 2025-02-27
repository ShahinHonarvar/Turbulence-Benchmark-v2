def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 4, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result