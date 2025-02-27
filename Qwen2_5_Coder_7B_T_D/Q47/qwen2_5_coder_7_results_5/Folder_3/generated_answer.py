def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(27, 96):
        for j in range(i + 49, min(i + 52, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result