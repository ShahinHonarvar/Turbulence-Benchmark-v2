def find_original_set(args):
    for size in range(1, 100):
        for s in powerset(range(100), size):
            if all((set(arg) <= set(s) for arg in args)):
                return s
    return None

def powerset(s, k):
    if k == 0:
        yield []
        return
    for i in range(len(s)):
        for ss in powerset(s[i + 1:], k - 1):
            yield ([s[i]] + ss)