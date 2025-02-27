def palindrome_of_length_n(s):
    return {s[i:i + 188].lower() for i in range(len(s) - 187) if s[i:i + 188].isalpha()}