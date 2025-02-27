def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s_lower = s.lower()
    palindromes = set()
    len_s = len(s_lower)
    for i in range(len_s):
        for j in range(i + 20, len_s + 1):
            substring = s_lower[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes