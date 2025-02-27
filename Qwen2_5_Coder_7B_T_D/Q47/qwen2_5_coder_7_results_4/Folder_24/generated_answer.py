def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(12, 93):
        for j in range(i + 42, min(93, i + 78)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result