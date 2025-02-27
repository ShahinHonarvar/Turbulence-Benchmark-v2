def palindrome_of_length_n(s):

    def is_palindrome(string):
        return string == string[::-1]
    palindromes = set()
    s = s.lower()
    len_s = len(s)
    for i in range(len_s):
        for j in range(i + 88, len_s + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes