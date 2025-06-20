def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    min_length = 26
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s)):
        for j in range(i + min_length, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes