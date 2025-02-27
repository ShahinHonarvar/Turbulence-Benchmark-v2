def palindromes_of_specific_lengths(s):
    lowered = s.lower()
    result = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for length in range(3, 7):
        for i in range(7 - length + 1):
            subs = lowered[i:i + length]
            if subs.isalpha() and is_palindrome(subs):
                result.add(subs)
    return result