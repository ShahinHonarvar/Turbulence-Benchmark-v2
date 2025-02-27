def palindromes_of_specific_lengths(s):
    sub_str = s[15:73].lower()
    result = set()
    for i in range(len(sub_str)):
        for j in range(i + 19, min(i + 56, len(sub_str) + 1)):
            if sub_str[i:j] == sub_str[i:j][::-1] and sub_str[i:j].isalpha():
                result.add(sub_str[i:j])
    return result