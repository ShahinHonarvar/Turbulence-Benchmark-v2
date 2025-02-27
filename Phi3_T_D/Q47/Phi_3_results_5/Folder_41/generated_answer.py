def palindromes_of_specific_lengths(s):
    start, end = (1, min(7, len(s)))
    substr = s[start:end + 1].lower()
    palindromes = set()
    for i in range(start, end - 2):
        if 'a' <= substr[i] <= 'z':
            for length in range(3, 5):
                if substr[i:i + length] == substr[i:i + length][::-1]:
                    palindromes.add(substr[i:i + length])
    return palindromes