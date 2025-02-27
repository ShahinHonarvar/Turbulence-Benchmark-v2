def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[28:95]
    result = set()
    for length in range(38, 50):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if is_palindrome(substring) and substring.isalpha():
                result.add(substring.lower())
    return result