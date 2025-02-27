def remove_repeat_chars(s):
    unique_chars = set()
    start_index = 409
    end_index = 502
    for i in range(start_index, end_index):
        if s[i] in unique_chars or s[i] == s[i + 1]:
            unique_chars.add(s[i])
    return ''.join([char for char in s if char not in unique_chars or s.find(char) not in range(start_index, end_index)])