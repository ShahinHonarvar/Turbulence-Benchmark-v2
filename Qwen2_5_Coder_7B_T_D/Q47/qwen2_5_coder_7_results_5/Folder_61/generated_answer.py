def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for i in range(len(s) - 19):
        for j in range(i + 20, min(len(s), i + 31)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result