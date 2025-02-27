def palindromes_of_specific_lengths(text):
    text = text.lower()
    valid_subtext = text[10:76]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(10, 21):
        for i in range(len(valid_subtext) - length + 1):
            substring = valid_subtext[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes