def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    result = set()
    for i in range(len(s) - 35):
        for j in range(i + 36, min(i + 43, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result