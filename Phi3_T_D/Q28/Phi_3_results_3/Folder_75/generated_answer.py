from bisect import bisect_left

def return_nth_smallest_ascii(s):
    candidates = sorted([ord(c) for c in s[62:84]])
    nth_smallest = candidates[8]
    return chr(nth_smallest)