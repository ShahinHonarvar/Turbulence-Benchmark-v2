def palindromes_of_specific_lengths(s):
    result = set()
    s = s[31:92].lower()
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 51]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 52]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 53]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result