# Add the functions in this file
def load_journal(jsonfile):
    import json
    with open(jsonfile, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())
    return data


def compute_phi(filename, event):
    import math
    n11, n00, n10, n01 = 0, 0, 0, 0
    n1p, n0p, np1, np0 = 0, 0, 0, 0
    journal = load_journal(filename)
    for i in range(91):
        if journal[i]['squirrel'] is true:
            np1 += 1
        else:
            np0 += 1
    for i in range(91):
        if event in journal[i]['events']:
            n1p += 1
            if journal[i]['squirrel'] is true:
                n11 += 1
            else:
                n10 += 1
        else:
            n0p += 1
            if journal[i]['squirrel'] is true:
                n01 += 1
            else:
                n00 += 1
    phi = (n11 * n00 - n10 * n01) / math.sqrt(n1p * n0p * np1 * np0)
    return phi


def compute_correlations(filename):
    correlation_dict = {}
    events = []
    journal = load_journal(filename)
    for i in range(91):
        for event in journal[i]['events']:
            if event not in events:
                events.append(event)
    for event in events:
        correlation_dict[event] = compute_phi(filename, event)
    return correlation_dict


def diagnose(filename):
    c_dict = compute_correlations(filename)
    keymax = max(c_dict, key=c_dict.get)
    keymin = min(c_dict, key=c_dict.get)
    return keymax, keymin


