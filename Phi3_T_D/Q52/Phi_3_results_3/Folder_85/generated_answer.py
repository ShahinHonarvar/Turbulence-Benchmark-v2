def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_n(text):
    results = set()
    length = 46
    text = text.lower()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if is_palindrome(substring):
            results.add(substring)
    return results