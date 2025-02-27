def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 31
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n - 1, length):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result