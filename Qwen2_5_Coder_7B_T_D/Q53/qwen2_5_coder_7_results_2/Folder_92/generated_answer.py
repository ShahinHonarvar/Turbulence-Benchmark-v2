def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 10
    palindrome_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set