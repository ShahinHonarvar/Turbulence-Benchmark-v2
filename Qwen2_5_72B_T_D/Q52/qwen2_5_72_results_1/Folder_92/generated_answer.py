def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes