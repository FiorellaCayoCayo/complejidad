def complejidad_ciclica(a, b, c):
    result = 0

    if a > 0:
        result += 1
        if b > 0:
            result += 1
            if c > 0:
                result += 1
            else:
                result += 2
        else:
            result += 3
            if c > 0:
                result += 1
            else:
                result += 2
    else:
        result += 4
        if b > 0:
            result += 1
        else:
            result += 2
            if c > 0:
                result += 1
            else:
                result += 2

    return result
