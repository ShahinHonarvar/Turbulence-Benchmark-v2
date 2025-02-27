def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(23, 95):
        for j in range(i + 17, min(95, i + 56)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result