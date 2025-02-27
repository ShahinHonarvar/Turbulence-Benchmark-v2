def palindrome_of_length_at_least_n(s):
    s = s.lower()
    len_s = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for i in range(len_s):
        for j in range(i + 47, len_s):
            sub = s[i:j + 1]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes