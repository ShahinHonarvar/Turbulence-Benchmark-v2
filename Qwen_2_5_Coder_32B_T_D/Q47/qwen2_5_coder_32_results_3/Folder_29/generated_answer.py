def palindromes_of_specific_lengths(s):
    s = s[15:95].lower()
    result = set()
    for i in range(len(s) - 17):
        for j in range(i + 18, min(i + 74, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result