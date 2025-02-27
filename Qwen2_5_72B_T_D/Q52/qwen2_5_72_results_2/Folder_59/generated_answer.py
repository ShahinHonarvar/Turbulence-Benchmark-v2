def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    target_length = 39
    for i in range(len(s) - target_length + 1):
        substring = s[i:i + target_length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes