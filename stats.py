def calc_words(text):
    return len(text.split())


def calc_symbols(text):
    m = {}
    for s in text:
        sc = s.lower()
        if sc in m:
            m[sc]+=1
        else:
            m[sc]=1
    return m