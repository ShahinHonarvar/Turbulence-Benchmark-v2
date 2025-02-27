def palindrome_of_length_n(s):

    def is_valid(char):
        return 'a' <= char <= 'z'
    results = set()
    s = s.lower()
    for i in range(len(s) - 172):
        substring = s[i:i + 173]
        if substring == substring[::-1] and all((is_valid(c) for c in substring)):
            results.add(substring)
    return results