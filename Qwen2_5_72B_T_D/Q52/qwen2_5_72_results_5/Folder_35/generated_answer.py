def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    length = 116
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes