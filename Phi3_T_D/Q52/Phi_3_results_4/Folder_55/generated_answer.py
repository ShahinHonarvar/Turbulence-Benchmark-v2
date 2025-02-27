def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 97] for i in range(len(s) - 96) if s[i:i + 97] == s[i:i + 97][::-1] and s[i:i + 97].isalpha()}