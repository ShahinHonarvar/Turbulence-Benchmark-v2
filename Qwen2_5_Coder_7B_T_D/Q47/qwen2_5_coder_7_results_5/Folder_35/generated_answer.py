def palindromes_of_specific_lengths(s):
    result = set()
    sub_str = s[34:91].lower()
    for length in range(14, 40):
        for i in range(len(sub_str) - length + 1):
            if sub_str[i:i + length] == sub_str[i:i + length][::-1] and sub_str[i:i + length].isalpha():
                result.add(sub_str[i:i + length])
    return result