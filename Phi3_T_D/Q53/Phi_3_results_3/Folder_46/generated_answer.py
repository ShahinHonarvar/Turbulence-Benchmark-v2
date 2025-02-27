def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 86, len(s) + 1):
            segment = s[i:j]
            if segment.isalpha():
                if segment == segment[::-1]:
                    palindromes.add(segment)
    return palindromes