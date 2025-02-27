def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length - 41):
        for j in range(i + 41, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result