def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95]
        if all((char.isalpha() for char in substring)) and is_palindrome(substring):
            result.add(substring)
    return result