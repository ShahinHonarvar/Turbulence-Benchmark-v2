def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 140
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes