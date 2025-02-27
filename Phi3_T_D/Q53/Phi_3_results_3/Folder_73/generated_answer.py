def palindrome_of_length_at_least_n(text):
    result = set()
    text_lower = text.lower()
    palindrome_cache = set()

    def is_palindrome(s):
        return s == s[::-1]
    for center in range(len(text_lower)):
        if text_lower[center].isalpha():
            expand_around_center(text_lower, center, center)
            expand_around_center(text_lower, center, center + 1)
    return {s for s in result if len(s) >= 94}

def expand_around_center(text_lower, left, right):
    low, high = (left, right)
    while low >= 0 and high < len(text_lower) and text_lower[low].isalpha() and text_lower[high].isalpha():
        if is_palindrome(text_lower[low:high + 1]):
            palindrome = text_lower[low:high + 1]
            palindrome_cache.add(palindrome)
            if len(palindrome) >= 94:
                result.add((palindrome, palindrome[::-1]))
        low -= 1
        high += 1