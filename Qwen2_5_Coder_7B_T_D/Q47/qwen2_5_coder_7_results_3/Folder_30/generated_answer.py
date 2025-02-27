def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(14, 91):
        for j in range(i + 54, min(91, i + 72)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result