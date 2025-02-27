def palindromes_of_specific_lengths(s):
    result = set()
    sub = s[32:72]
    for i in range(len(sub) - 20):
        for j in range(i + 20, len(sub) + 1):
            substring = sub[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha() and (21 <= len(substring) <= 32):
                result.add(substring)
    return result