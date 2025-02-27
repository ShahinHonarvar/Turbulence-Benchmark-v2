def palindromes_of_specific_lengths(s):
    palindromes = set()
    window_size_range = range(20, 22)
    for i in range(12, 57):
        for j in range(i + min(window_size_range), i + max(window_size_range) + 1):
            window = s[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes