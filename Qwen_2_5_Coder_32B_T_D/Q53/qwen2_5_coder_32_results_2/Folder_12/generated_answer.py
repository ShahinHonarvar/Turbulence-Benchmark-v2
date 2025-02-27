def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(i + 51, len(s) + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(substring) and len(substring) >= 51:
                palindromes.add(substring)
    return palindromes