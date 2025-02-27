def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 19, length + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes