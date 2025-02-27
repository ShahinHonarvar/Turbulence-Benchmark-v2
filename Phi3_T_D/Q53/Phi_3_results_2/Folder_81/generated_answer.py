def palindrome_of_length_at_least_n(s):
    results = set()
    s_lower = s.lower()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for center in range(len(s_lower)):
        for length in range(33, len(s_lower) - center + 1):
            if is_palindrome(s_lower[center:center + length]):
                results.add(s_lower[center:center + length])
    return results