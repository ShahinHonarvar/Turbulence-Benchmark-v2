def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    result = set()
    for i in range(len(s) - 49):
        for j in range(i + 49, min(i + 100, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result