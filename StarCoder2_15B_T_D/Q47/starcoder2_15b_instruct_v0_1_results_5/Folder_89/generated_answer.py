def palindromes_of_specific_lengths(string):
    sub_string = string[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(sub_string) - length + 1):
            candidate = sub_string[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes