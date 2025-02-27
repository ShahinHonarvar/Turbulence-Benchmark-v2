def palindromes_of_specific_lengths(s):
    result = set()
    s = s[39:95].lower()
    for i in range(len(s)):
        for j in range(i + 14, min(len(s), i + 53)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result