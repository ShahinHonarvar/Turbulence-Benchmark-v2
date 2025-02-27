def palindrome_of_length_n(text):

    def is_palindrome(text):
        return text == text[::-1]

    def get_substrings_of_length_n(text, n):
        return [text[i:i + n] for i in range(len(text) - n + 1)]

    def filter_palindromes(substrings):
        return [substring for substring in substrings if is_palindrome(substring)]

    def filter_english_letters(text):
        return ''.join([char for char in text if char.isalpha()])

    def to_lowercase(text):
        return text.lower()
    substrings = get_substrings_of_length_n(text, 47)
    palindromes = filter_palindromes(substrings)
    palindromes = [filter_english_letters(palindrome) for palindrome in palindromes]
    palindromes = [to_lowercase(palindrome) for palindrome in palindromes]
    return set(palindromes)