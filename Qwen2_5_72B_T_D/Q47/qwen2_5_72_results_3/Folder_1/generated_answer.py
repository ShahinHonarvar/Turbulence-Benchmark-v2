def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[15:90].lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 40, min(i + 73, len(text) + 1)):
            substring = text[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes