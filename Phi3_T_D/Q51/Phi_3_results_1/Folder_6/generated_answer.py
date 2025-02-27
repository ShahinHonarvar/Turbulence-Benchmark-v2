def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        s_norm = ''.join(sorted(s.lower()))
        if len(s) < 3:
            continue
        if s_norm in anagrams:
            anagrams[s_norm].append(s)
        else:
            anagrams[s_norm] = [s]
    count = 0
    keys = list(anagrams.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[i] == keys[j]:
                count += 1
                if count > 86:
                    return False
    return True