def if_contains_anagrams(lst):

    def create_signature(s):
        return ''.join(sorted(s.lower()))
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (create_signature(lst[i]) == create_signature(lst[j])):
                pairs += 1
                if pairs >= 42:
                    return True
    return False