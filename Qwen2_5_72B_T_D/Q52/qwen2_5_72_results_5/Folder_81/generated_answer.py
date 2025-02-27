def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    n = 99
    if n > len(s):
        return palindromes
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes