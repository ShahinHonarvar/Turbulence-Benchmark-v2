def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[119:257]
    text = ''.join([char for char in text if char.isalpha()])
    result = set()
    for length in range(104, 124):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if is_palindrome(substring):
                result.add(substring.lower())
    return result