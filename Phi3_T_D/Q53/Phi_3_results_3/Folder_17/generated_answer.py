def palindrome_of_length_at_least_n(s):
    strings = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 36, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                strings.add(substring)
    return strings