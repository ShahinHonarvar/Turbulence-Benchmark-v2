def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 90][::-1] for i in range(len(s) - 89) if 'a' <= s[i] <= 'z'}