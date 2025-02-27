def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return 'a' <= c <= 'z'

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    return set(filter(is_english_letter, (s[i:i + j] for i in range(10, 71) for j in range(24, 53) if is_palindrome(s[i:i + j]))))