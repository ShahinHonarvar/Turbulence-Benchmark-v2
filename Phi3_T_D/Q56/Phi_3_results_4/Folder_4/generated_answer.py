from itertools import islice

def all_substring_of_size_n(s):
    subtlen = 41
    length = len(s)
    result = set()
    for i in range(length - subtlen + 1):
        if len(set(s[i:i + subtlen])) == subtlen:
            result.add(s[i:i + subtlen])
    return list(result)