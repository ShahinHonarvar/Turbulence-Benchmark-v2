def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes