def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(12, min(len(s), 123)):
        for j in range(i, min(len(s), i + 221)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result