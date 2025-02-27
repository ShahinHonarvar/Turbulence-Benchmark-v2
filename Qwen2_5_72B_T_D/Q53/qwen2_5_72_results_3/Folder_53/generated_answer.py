def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s_len = len(s)
    for i in range(s_len):
        for j in range(i + 63, s_len):
            substr = s[i:j + 1]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes