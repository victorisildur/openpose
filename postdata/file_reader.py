def read_x_y_score_list(filename):
    f = open(filename)
    line = f.readline()
    print(line)
    t = []
    xys = []
    i = 0
    while line:
        part = i % 25
        xyscore = line.split()
        xyscore[0] = float(xyscore[0])
        xyscore[1] = float(xyscore[1])
        xyscore[2] = float(xyscore[2])
        if part == 0:
            t.append(i)
        if len(xys) <= part:
            xys.append([xyscore])
        else:
            xys[part].append(xyscore)
        line = f.readline()
        i+=1
    f.close()
    return t, xys