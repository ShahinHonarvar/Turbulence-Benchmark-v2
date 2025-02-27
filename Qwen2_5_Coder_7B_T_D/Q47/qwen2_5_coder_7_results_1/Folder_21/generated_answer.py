def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(100, 296):
        for j in range(i + 136, min(i + 161, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result