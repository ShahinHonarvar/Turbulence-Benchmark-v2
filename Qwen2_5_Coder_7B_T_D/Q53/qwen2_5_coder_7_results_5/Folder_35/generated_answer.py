def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(i + 25, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes