def palindromes_of_specific_lengths(s):
    window_range = range(75, 96)
    eligible_palindromes = set()
    for i in window_range:
        if not s[i].isalpha():
            continue
        for length in range(7, 10):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                eligible_palindromes.add(substring)
    return eligible_palindromes