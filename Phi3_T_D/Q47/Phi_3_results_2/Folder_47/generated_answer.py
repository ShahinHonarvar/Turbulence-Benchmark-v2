def palindromes_of_specific_lengths(s):
    start, end = (39, 94)
    valid_lengths = list(range(14, 53))
    substr = s[start:end + 1].lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    return {sub for sub in (substr[i:i + l] for i in range(len(substr)) for l in valid_lengths) if sub.isalpha() and is_palindrome(sub)}