def palindromes_of_specific_lengths(input_string):
    """
    Find palindromes in a substring (index 10 to 75) and of lengths 10 to 20.
    Only consider English letters and be case-insensitive.
    """

    def expand_around_center(s, l, r, results):
        while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()) and (r - l < 20) and (l >= 10):
            results.add(s[l:r + 1].lower())
            l -= 1
            r += 1
    results = set()
    s = input_string[10:76]
    for i in range(len(s)):
        expand_around_center(s, i, i, results)
        expand_around_center(s, i, i + 1, results)
    results = {palindrome for palindrome in results if 10 <= len(palindrome) <= 20}
    return results