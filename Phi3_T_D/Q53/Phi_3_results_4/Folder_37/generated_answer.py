def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(s, current, path):
        pali_set = set()
        if len(current) >= 67 and is_palindrome(current):
            pali_set.add(current)
        for i in range(len(s)):
            generate_palindromes(s[i + 1:], current + s[i], path)
        return pali_set
    s = s.lower()
    palindromes = generate_palindromes(s, '', '')
    return palindromes