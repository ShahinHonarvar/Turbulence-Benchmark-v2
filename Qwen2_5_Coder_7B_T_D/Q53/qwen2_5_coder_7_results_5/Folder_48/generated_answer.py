def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 150
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result