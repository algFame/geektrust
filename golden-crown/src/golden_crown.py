emblem = {'SPACE': 'GORILLA', 'LAND': 'PANDA', 'WATER': 'OCTOPUS', 'AIR': 'OWL', 'ICE': 'MAMMOTH', 'FIRE': 'DRAGON'}


def shift(a, k):
    alphabets = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    a = list(a)
    for i in range(len(a)):
        if a[i] in alphabets:
            __ = alphabets.index(a[i])
            a[i] = alphabets[(__ - k) % 26]
    return ''.join(a)


def check(kingdom, secret_msg):
    decoded = shift(secret_msg, len(emblem[kingdom]))
    dict_msg = {}
    for i in decoded:
        if i not in dict_msg:
            dict_msg[i] = 1
        else:
            dict_msg[i] += 1
    for i in emblem[kingdom]:
        if i in dict_msg and dict_msg[i] > 0:
            dict_msg[i] -= 1
        else:
            return None
    return kingdom


def ruler(input: list):
    allies = []
    for i in input:
        i = i.split()
        _ = check(i[0], ''.join(i[1:]))
        if _ != None: allies.append(_)
    if len(set(allies)) >= 3: return f'''SPACE {' '.join(allies)}'''
