def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    half_window = 54
    max_length = 58
    palindromes = set()
    for i in range(33, len(text) - max_length + 1):
        window = text[i - half_window:i + half_window + 1]
        for length in range(103, 159):
            if length % 2 == 0:
                start = i - length // 2
                end = i + length // 2 + 1
            else:
                start = i - length // 2
                end = i + length // 2 + 1
            if all((char.isalpha() for char in window[start:end])) and is_palindrome(window[start:end].lower()):
                palindromes.add(window[start:end].lower())
            start, end = (start + 1, end + 1)
    return palindromes