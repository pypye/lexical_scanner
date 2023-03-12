non_symbols = ['+', '*', '.', '|', '(', ')']

def precedence_comparator(a, b):
    p = ["|", "+", ".", "*"]
    return p.index(a) > p.index(b)

def add_concationate(regex):
    res = []
    for i in range(len(regex)-1):
        res.append(regex[i])
        if regex[i] not in non_symbols:
            if regex[i + 1] not in non_symbols or regex[i + 1] == '(':
                res += '.'
        if regex[i] in [')', '*', '+'] and regex[i + 1] == '(':
            res += '.'
        if regex[i] in [')', '*', '+'] and regex[i + 1] not in non_symbols:
            res += '.'
    res += regex[-1]
    return "".join(res)

def make_polish_postfix(regex):
    s = []
    res = ""
    for c in regex:
        if c not in non_symbols or c == "*" or c == "+":
            res += c
        elif c == ")":
            while len(s) > 0 and s[-1] != "(": res += s.pop()
            s.pop()
        elif c == "(":
            s.append(c)
        elif len(s) == 0 or s[-1] == "(" or precedence_comparator(c, s[-1]):
            s.append(c)
        else:
            while len(s) > 0 and s[-1] != "(" and not precedence_comparator(c, s[-1]): res += s.pop()
            s.append(c)
    while len(s) > 0: res += s.pop()
    return res

def regex_parser(data):
    data = add_concationate(data)
    data = make_polish_postfix(data)
    return data