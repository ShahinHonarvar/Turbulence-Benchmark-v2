def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 49, min(i + 52, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result