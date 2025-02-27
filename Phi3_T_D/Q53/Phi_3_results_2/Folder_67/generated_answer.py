def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    return {s[i:j] for i in range(length) for j in range(i + 25, length + 1) if s[i:j] == s[i:j][::-1]}