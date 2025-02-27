def remove_repeat_chars(s):

    def count_chars(sub_s):
        char_count = {}
        for char in sub_s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    sub_string = s[36:85]
    char_count = count_chars(sub_string)
    result = ''.join([char for char in s if char not in char_count or char_count[char] == 1])
    return result