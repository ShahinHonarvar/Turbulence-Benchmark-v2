def is_palindrome(s):
    return s == s[::-1]

def get_all_substrings(s):
    length = len(s)
    return [s[i:j + 1] for i in range(length) for j in range(i, length)]

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters_only = ''.join(filter(str.isalpha, string))
    substrings = get_all_substrings(letters_only)
    palindromes = {sub for sub in substrings if len(sub) >= 24 and is_palindrome(sub)}
    return palindromes