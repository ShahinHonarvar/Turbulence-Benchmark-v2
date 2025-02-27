def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 136, len(s)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes