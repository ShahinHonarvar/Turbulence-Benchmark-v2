def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def generate_palindromes(s, start, end, length, results):
    if length == 0:
        if is_palindrome(search_str):
            results.add(search_str.lower())
        return
    for i in range(start, min(end, len(s))):
        generate_palindromes(s, i + 1, end, length - 1, results)
        search_str = s[start:i + 1]
        if is_palindrome(search_str):
            results.add(search_str.lower())

def palindromes_of_specific_lengths(s):
    start, end, min_length, max_length = (26, 88, 52, 57)
    results = set()
    for length in range(min_length, max_length + 1):
        generate_palindromes(s, start, end, length, results)
    filtered_results = {palindrome for palindrome in results if palindrome.isalpha()}
    return filtered_results