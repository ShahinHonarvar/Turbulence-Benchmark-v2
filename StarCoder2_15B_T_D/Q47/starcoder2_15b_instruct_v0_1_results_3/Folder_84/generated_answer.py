def palindromes_of_specific_lengths(s):
    palindromes = set()
    start_index = 23
    end_index = 77
    for length in range(13, 41):
        for i in range(start_index, end_index - length + 1):
            window = s[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes