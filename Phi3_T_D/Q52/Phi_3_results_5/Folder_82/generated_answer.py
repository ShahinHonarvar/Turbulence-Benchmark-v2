def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 27):
        palindrome_candidate = s[i:i + 28]
        if is_palindrome(palindrome_candidate):
            palindromes.add(palindrome_candidate)
    return palindromes