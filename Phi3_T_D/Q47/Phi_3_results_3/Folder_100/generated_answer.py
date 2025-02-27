def palindromes_of_specific_lengths(s):
    start, end = (29, min(96, len(s)))
    s = s.lower()
    palindromes = set()

    def is_palindrome_of_length(sub, length):
        for i in range(length // 2):
            if sub[i] != sub[length - 1 - i]:
                return False
        return True
    for length in range(12, 19):
        for i in range(start, end + 1 - length):
            if is_palindrome_of_length(s[i:i + length], length):
                palindromes.add(s[i:i + length])
    return palindromes