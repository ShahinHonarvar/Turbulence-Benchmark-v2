def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    result = set()
    for start in range(len(s) - 19):
        for end in range(start + 19, min(start + 67, len(s) + 1)):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result