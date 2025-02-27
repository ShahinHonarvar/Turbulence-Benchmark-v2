def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    result = set()
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if substring == substring[::-1]:
            result.add(substring)
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if substring == substring[::-1]:
            result.add(substring)
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1]:
            result.add(substring)
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1]:
            result.add(substring)
    return result