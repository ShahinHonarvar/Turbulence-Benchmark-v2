def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    length = 47
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + length, len(s_lower) + 1):
            segment = s_lower[i:j]
            if segment == segment[::-1]:
                if all((c.isalpha() for c in segment)):
                    palindromes.add(segment)
    return palindromes