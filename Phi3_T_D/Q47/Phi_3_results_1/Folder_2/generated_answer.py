def palindromes_of_specific_lengths(text):

    def is_english_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    length_limit_start, length_limit_end = (18, 36)
    substr = text[10:60].lower()
    for length in range(length_limit_start, length_limit_end + 1):
        for start in range(len(substr) - length + 1):
            substr_segment = substr[start:start + length]
            if all((is_english_letter(c) for c in substr_segment)) and is_palindrome(substr_segment):
                palindromes.add(substr_segment)
    return palindromes