def palindrome_of_length_n(s):
    return {s[i:i + 35].lower() for i in range(len(s) - 34) if s[i:i + 35].lower() == s[i:i + 35].lower()[::-1]}