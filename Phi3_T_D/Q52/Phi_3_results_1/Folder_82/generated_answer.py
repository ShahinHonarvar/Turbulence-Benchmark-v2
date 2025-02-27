def palindrome_of_length_n(s):
    s = s.lower()
    result_set = {s[i:i + 28] for i in range(len(s) - 27) if s[i:i + 28] == s[i:i + 28][::-1]}
    return {substring.upper() for substring in result_set}