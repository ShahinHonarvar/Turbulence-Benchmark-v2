def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 99] for i in range(len(s) - 98) if s[i:i + 99] == s[i:i + 99][::-1] and s[i:i + 99].isalpha()}