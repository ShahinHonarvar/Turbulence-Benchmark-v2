def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 distinct arguments are required.')
    main_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets.')
        main_set |= s
    return main_set