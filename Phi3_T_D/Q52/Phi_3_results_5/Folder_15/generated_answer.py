def palindrome_of_length_n(s):
    s_lower = s.lower()
    n = 4
    return {s_lower[i:i + n] for i in range(len(s_lower) - n + 1) if s_lower[i:i + n] == s_lower[i:i + n][::-1] and s_lower[i:i + n].isalpha()}