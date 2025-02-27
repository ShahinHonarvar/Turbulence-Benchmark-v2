def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:76].lower()
    for i in range(len(s)):
        for j in range(i + 10, min(len(s) + 1, i + 21)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result