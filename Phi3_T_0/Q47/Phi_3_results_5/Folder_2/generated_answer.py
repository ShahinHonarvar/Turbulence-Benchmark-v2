def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def valid_length(sub):
        return 18 <= len(sub) <= 36

    def is_english_letters(sub):
        return all(('a' <= c.lower() <= 'z' for c in sub))
    palindromes = set()
    for length in range(18, 37):
        for i in range(10, 60 - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub) and valid_length(sub) and is_english_letters(sub):
                palindromes.add(sub.lower())
    return palindromes