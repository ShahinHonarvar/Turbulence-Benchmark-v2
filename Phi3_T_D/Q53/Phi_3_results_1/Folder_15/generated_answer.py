def palindrome_of_length_at_least_n(s):

    def is_letters(s):
        return s.isalpha()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    len_s = len(s)
    for start in range(len_s):
        for end in range(start + 3, len_s):
            chunk = s[start:end + 1]
            if is_letters(chunk) and is_palindrome(chunk.lower()):
                palindromes.add(chunk.lower())
    return palindromes