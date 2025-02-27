def is_palindrome(s, left, right):
    return s[left:right].lower() == s[left:right].lower()[::-1]

def palindrome_of_length_n(s):
    length = 34
    palindromes = set()
    for i in range(len(s) - length + 1):
        if is_palindrome(s, i, i + length):
            palindromes.add(s[i:i + length])
    return palindromes