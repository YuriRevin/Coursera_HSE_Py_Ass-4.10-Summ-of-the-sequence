l = []


def ss(n, i):
    if n != 0:
        l.append(n)
        return ss(int(input()), i+1)
    else:
        if i == 0 and n == 0:
            return '0'
        else:
            k = l[0]
            for i in range(1, i):
                k = k + l[i]
            return k


print(ss(int(input()), 0))
