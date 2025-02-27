def palindromes_of_specific_lengths(string):
    sub_string = string[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(sub_string) - length + 1):
            s = sub_string[i:i + length]
            if s.lower() == s[::-1].lower():
                palindromes.add(s)
    return palindromes