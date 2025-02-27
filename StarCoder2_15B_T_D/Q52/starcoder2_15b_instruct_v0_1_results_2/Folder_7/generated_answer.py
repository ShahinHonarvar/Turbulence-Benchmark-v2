def palindrome_of_length_n(s):
    result = set()
    n = 416
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result