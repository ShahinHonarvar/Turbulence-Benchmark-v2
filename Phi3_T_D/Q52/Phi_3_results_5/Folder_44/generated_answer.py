def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 444):
        if is_palindrome(s[i:i + 445]):
            palindromes.add(s[i:i + 445])
    return palindromes