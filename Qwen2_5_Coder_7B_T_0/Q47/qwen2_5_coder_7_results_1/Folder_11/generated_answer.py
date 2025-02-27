def palindromes_of_specific_lengths(s):
    result = set()
    s = s[24:98].lower()
    for i in range(len(s)):
        for j in range(i + 10, min(len(s), i + 37)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result