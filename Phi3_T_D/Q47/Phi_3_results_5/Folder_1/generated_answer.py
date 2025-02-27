def palindromes_of_specific_lengths(s):
    upper_idx = 15
    lower_idx = 89
    result = set()
    for length in range(40, 73):
        for i in range(upper_idx, lower_idx - length + 1):
            substring = s[i:i + length]
            if substring.isalpha():
                if substring.lower() == substring[::-1].lower():
                    result.add(substring)
    return result