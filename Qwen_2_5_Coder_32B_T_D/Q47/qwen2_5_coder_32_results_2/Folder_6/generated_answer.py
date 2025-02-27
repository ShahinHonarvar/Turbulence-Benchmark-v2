def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    result = set()
    for i in range(len(s) - 39):
        for j in range(i + 40, min(i + 48, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result