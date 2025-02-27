def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 472] for i in range(len(s) - 471) if s[i:i + 472] == s[i:i + 472][::-1]}