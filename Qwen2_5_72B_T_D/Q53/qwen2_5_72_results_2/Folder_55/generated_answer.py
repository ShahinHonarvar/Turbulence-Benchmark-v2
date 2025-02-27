def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s)):
        for j in range(i + 82, len(s)):
            sub = s[i:j + 1]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes