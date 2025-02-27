def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    length = 25
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes