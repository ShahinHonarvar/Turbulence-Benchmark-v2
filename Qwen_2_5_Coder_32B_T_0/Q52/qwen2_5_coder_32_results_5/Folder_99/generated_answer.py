def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 419):
        substring = s[i:i + 420]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result