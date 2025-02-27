def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s) - 93):
        substr = s[i:i + 94]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes