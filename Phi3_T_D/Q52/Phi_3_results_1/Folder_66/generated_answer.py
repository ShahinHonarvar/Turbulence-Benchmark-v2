def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    length = 25
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - length + 1):
        sub = s_lower[i:i + length]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes