def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def extract_letters_only(text):
        return ''.join([char for char in text if char.isalpha()])
    s = extract_letters_only(s[:101].lower())
    result = set()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if is_palindrome(word):
                result.add(word)
    return result