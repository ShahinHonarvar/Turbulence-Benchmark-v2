def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, len(s)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1].upper())
    return palindromes