def palindromes_of_specific_lengths(text):
    lower_bound, upper_bound = (40, 94)
    length_range = range(45, 52)
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')

    def is_palindrome(s):
        return s == s[::-1]
    candidates = []
    for length in length_range:
        for i in range(lower_bound, upper_bound - length + 2):
            if text[i:i + length].lower() == text[i:i + length].lower():
                candidates.append(text[i:i + length])
    palindromes = set(filter(lambda s: set(s.lower()).issubset(valid_chars) and is_palindrome(s.lower()), candidates))
    return palindromes