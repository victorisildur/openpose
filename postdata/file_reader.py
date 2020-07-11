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
        try:
            xyscore[0] = float(xyscore[0])
            xyscore[1] = float(xyscore[1])
            xyscore[2] = float(xyscore[2])
            if part == 0:
                t.append(i)
            if len(xys) <= part:
                xys.append([xyscore])
            else:
                xys[part].append(xyscore)
            i += 1
        except:
            print()
        finally:
            line = f.readline()
    f.close()
    return t, xys
