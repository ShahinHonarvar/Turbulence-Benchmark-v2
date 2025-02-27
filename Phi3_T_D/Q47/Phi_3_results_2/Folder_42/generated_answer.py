def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    sub_str = s[42:96].lower()
    return {sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 18, min(i + 47 + 1, len(sub_str) + 1)) if is_palindrome(sub_str[i:j]) and sub_str[i:j].isalpha()}