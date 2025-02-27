def palindromes_between_indices(s):
    subset = s[7:9]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for char1 in unique_chars:
        for char2 in unique_chars:
            for char3 in unique_chars:
                palindrome = char1 + char2 + char3 + char2 + char1
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes