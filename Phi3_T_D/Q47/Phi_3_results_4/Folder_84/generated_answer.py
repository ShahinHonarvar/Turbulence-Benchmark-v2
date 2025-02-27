def palindromes_of_specific_lengths(s):
    start_idx, end_idx = (23, 77)
    palindromes = set()

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    for l in range(13, 41):
        for i in range(start_idx, end_idx + 1 - l + 1):
            sub = s[i:i + l]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes