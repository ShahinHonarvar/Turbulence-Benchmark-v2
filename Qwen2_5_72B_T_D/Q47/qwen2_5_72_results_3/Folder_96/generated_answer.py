def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[100:301]
    text = ''.join(filter(str.isalpha, text))
    found_palindromes = set()
    for i in range(len(text)):
        for j in range(i + 49, min(i + 101, len(text))):
            substring = text[i:j + 1].lower()
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes