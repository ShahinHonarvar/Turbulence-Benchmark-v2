def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes