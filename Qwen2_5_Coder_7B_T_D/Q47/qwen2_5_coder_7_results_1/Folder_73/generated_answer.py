def palindromes_of_specific_lengths(s):
    result = set()
    s = s[21:63].lower()
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 30):
        substring = s[i:i + 31]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result