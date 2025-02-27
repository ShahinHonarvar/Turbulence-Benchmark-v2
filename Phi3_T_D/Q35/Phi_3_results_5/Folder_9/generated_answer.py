from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[80:200])
    s_list = list(s)
    for i in range(80, 200):
        if counter[s[i]] > 1:
            s_list[i] = ''
    return ''.join(s_list)