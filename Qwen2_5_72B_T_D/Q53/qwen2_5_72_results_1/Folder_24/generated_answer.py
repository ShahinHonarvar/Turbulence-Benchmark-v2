def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    found_palindromes = set()
    for i in range(n):
        for j in range(i + 52, n):
            if is_palindrome(s[i:j + 1]):
                found_palindromes.add(s[i:j + 1])
    return found_palindromes