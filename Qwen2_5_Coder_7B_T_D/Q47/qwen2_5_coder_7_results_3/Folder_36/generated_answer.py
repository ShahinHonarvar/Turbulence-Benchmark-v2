def palindromes_of_specific_lengths(s):
    result = set()
    s = s[124:284].lower()
    for start in range(len(s) - 114):
        for length in range(115, 135):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result