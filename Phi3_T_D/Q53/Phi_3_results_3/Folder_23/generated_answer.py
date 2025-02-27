def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    potential_palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 19, len(s) + 1)}
    palindromes = {pal for pal in potential_palindromes if is_palindrome(pal)}
    return palindromes