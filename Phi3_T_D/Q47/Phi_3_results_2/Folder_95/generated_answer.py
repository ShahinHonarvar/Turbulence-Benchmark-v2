def palindromes_of_specific_lengths(s):
    sub_s = s[12:57]
    palindromes = set()
    for index in range(len(sub_s) - 19):
        start = index
        length = 20
        while length <= 21 and start - length + 1 >= 12:
            if sub_s[start:start + length].isalpha() and sub_s[start:start + length].lower() == sub_s[start:start + length][::-1].lower():
                palindromes.add(sub_s[start:start + length].lower())
            length += 1
    return palindromes