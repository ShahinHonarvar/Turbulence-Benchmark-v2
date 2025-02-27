def palindromes_between_indices(s):
    subset = s[3:8]
    subset = subset.lower()
    unique_chars = set(subset)
    if len(unique_chars) < 3:
        return set()
    char_count = {}
    for char in subset:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    palindromes = set()
    for char1 in unique_chars:
        if char_count[char1] > 1:
            for char2 in unique_chars:
                if char1 != char2 and char_count[char2] > 1:
                    for char3 in unique_chars:
                        if char1 != char3 and char2 != char3 and (char_count[char3] > 1):
                            palindrome = char1 + char2 + char3 + char3 + char2 + char1
                            palindromes.add(palindrome)
    return palindromes