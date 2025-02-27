def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    set_of_palindromes = set()
    length = len(s)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for start in range(length):
        for end in range(start + 56, length + 1):
            sub = s[start:end].lower()
            if all((c in alphabet for c in sub)) and is_palindrome(sub):
                set_of_palindromes.add(sub)
    return set_of_palindromes