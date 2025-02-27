def palindromes_of_specific_lengths(s):
    sub_s = s[24:98].lower()
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(sub_s) - length + 1):
            chunk = sub_s[i:i + length]
            if chunk.isalpha() and chunk == chunk[::-1]:
                palindromes.add(chunk)
    return palindromes