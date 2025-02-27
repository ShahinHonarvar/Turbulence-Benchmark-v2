def palindrome_of_length_n(s):

    def is_letter(c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

    def get_substrings(s):
        length = len(s)
        return (s[i:j + 1] for i in range(length) for j in range(i + 1, length))

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    for substring in get_substrings(s):
        if len(substring) == 113 and all((is_letter(c) for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes