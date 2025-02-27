def palindromes_of_specific_lengths(s):
    result = set()
    s = s[18:89].lower()
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 13]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 14]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result