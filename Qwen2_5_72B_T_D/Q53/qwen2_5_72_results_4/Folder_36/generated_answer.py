def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    n = 144
    s_length = len(s)
    for i in range(s_length):
        for j in range(i + n, s_length + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes