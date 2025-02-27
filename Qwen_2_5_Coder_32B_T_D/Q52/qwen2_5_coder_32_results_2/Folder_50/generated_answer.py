def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result