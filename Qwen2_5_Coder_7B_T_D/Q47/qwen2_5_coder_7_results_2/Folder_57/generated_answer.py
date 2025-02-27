def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 39, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result