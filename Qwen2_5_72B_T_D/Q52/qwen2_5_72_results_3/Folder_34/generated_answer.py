def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes