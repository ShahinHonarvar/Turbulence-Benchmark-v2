def palindrome_of_length_at_least_n(s):
    return {s[i:j] for i in range(len(s)) for j in range(i + 3, len(s) + 1) if s[i:j].lower() == s[i:j][::-1] and s[i:j].isalpha()}