def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + 121, length):
            sub = s[i:j + 1]
            if is_palindrome(sub) and sub.isalpha() and (len(sub) >= 122):
                palindromes.add(sub)
    return palindromes