def all_right_truncatable_prime(args):
    x = args[28]
    rtp = []
    for n in range(2, x):
        is_rtp = True
        for i in range(len(str(n)) - 1):
            if int(str(n)[i + 1:]) % n != 0:
                is_rtp = False
                break
        if is_rtp:
            rtp.append(n)
    rtp.sort()
    return rtp