def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    s_lower = s.lower()
    s_len = len(s_lower)
    palindrome_set = set()
    for i in range(s_len - 83):
        if is_palindrome(s_lower[i:i + 84]):
            palindrome_set.add(s_lower[i:i + 84])
    return palindrome_set