def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if substring == substring[::-1]:
            result.add(substring)
    return result