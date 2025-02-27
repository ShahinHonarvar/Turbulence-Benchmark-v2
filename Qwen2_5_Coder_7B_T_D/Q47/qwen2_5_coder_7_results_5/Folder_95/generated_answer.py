def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(12, 57):
        for j in range(i + 20, min(57, i + 22)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result