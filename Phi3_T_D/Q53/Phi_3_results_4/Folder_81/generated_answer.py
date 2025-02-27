from re import findall
    from string import ascii_letters

def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    potential_palindromes = findall(f'[a-zA-Z]{{33,}}', text.lower())
    return {p for p in potential_palindromes if is_palindrome(p)}