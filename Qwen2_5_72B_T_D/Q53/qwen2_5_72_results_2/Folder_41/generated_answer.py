def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s)):
        for j in range(i + 27, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes