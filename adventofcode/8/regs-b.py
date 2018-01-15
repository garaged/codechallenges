import re 
def read_regs(file):
    f = open(file, "r")
    lines_l = f.readlines()
    p = re.compile('(\w+)\s+(\w+)\s+(-?\w+)\s+(\w+\s+(\w+)\s.+)$')
                # b inc 5 if a > 1
    regs = {}
    cnt = 0
    at_max = 0
    for line_i in lines_l:
        cnt += 1
        m = p.match(line_i)
        d = m.groups()
        if eval("'{}' not in regs".format(d[4])):
            exec("regs['{}'] = 0".format(d[4]))
        if eval("'{}' not in regs".format(d[0])):
            exec("regs['{}'] = 0".format(d[0]))
        new_expr = d[3].replace(" {} ".format(d[4]), " regs['{}'] ".format(d[4]),1).replace("if ", "",1)
        test = eval(new_expr)
        if test:
            if d[1] == "inc":
                op = "+="
            else:
                op = '-='
            try:
                exec("regs['{}'] {} {}".format(d[0], op, d[2]))
            except:
                exec("regs['{}'] = 0".format(d[0]))
        v_max = max(regs.keys(), key=(lambda k: regs[k]))
        if regs[v_max] > at_max:
            at_max = regs[v_max]
    return regs, at_max
            
regs, at_max = read_regs("regs.txt")
v_max = max(regs.keys(), key=(lambda k: regs[k]))
print(regs[v_max], at_max)
