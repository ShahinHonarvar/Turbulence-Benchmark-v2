def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text_sub = text[124:284]
    palindromes = set()
    for length in range(115, 135):
        for start in range(len(text_sub) - length + 1):
            substring = text_sub[start:start + length]
            if is_palindrome(substring) and substring.isalpha() and (substring.lower() == substring.upper()):
                palindromes.add(substring.lower())
    return palindromes