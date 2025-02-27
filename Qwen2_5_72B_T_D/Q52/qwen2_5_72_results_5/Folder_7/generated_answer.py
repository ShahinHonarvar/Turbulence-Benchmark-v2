def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    n = 416
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes