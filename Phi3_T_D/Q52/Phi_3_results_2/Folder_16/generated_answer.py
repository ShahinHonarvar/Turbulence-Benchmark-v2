def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set((s[i:i + 255] for i in range(len(s) - 254) if s[i:i + 255] == s[i:i + 255][::-1]))
    return palindromes