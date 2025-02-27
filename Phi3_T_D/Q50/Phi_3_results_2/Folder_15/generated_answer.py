def if_contains_anagrams(string_list):
    count = 0
    processed = []
    for s in string_list:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        for p in processed:
            if sorted_s == p:
                count += 1
                break
        else:
            processed.append(sorted_s)
        if count >= 4:
            return True
    return False