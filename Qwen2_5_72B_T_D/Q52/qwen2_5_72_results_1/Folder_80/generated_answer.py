def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    length = len(s)
    target_length = 276
    palindromes = set()
    for i in range(length - target_length + 1):
        substring = s[i:i + target_length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes