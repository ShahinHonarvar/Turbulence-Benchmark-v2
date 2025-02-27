def remove_repeat_chars(s):
    index_limit = (33, 78)
    char_count = {}
    for i, char in enumerate(s[index_limit[0]:index_limit[1]]):
        char_count[char] = char_count.get(char, 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 0) <= 1 or index_limit[0] <= s.index(char) < index_limit[1]])
    return result