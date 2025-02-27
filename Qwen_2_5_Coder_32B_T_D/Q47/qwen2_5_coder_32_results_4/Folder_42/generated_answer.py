def palindromes_of_specific_lengths(s):
    s = s[43:96].lower()
    result = set()
    for start in range(len(s) - 17):
        for end in range(start + 18, min(start + 48, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result