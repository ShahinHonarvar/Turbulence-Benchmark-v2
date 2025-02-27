def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    result = set()
    for start in range(len(s) - 49):
        for end in range(start + 50, min(start + 101, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result