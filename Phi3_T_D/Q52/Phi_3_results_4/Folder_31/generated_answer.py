def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 66] for i in range(len(s) - 65) if s[i:i + 66].isalpha() and s[i:i + 66] == s[i:i + 66][::-1]}