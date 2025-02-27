def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    start, end = (75, 95)
    if end > len(s) - 1:
        end = len(s) - 1
    for i in range(start, end + 1):
        for length in range(7, 10):
            if i + length - 1 <= end:
                sub = s[i:i + length]
                if sub.isalpha() and is_palindrome(sub):
                    result.add(sub)
    return result