def palindromes_of_specific_lengths(s):
    sub_s = s[106:281]
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(1, len(sub_s) - i + 1):
            substring = sub_s[i:i + j]
            if len(substring) >= 136 and len(substring) <= 151 and substring.isalpha():
                low_case = substring.lower()
                if low_case == low_case[::-1]:
                    palindromes.add(substring)
    return palindromes