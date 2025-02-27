def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s) - 41):
        sub = s[i:i + 42]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes