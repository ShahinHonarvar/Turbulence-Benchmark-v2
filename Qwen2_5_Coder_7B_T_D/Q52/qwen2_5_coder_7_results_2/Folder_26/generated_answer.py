def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 366, n + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result