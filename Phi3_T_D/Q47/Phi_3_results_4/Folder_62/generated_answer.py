def palindromes_of_specific_lengths(s):
    sub_str = s[26:88]
    return {sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 52, min(i + 57, len(sub_str) + 1)) if sub_str[i:j].isalpha() and sub_str[i:j].lower() == sub_str[i:j][::-1]}