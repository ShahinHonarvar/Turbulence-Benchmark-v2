def palindromes_of_specific_lengths(s):
    result = set()
    sub_str = s[103:277].lower()
    for i in range(len(sub_str)):
        for j in range(i + 100, min(len(sub_str), i + 170)):
            if sub_str[i:j] == sub_str[i:j][::-1]:
                result.add(sub_str[i:j])
    return result