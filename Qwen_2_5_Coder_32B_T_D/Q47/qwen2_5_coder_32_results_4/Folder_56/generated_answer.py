def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs)
    return palindromes