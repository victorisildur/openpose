import matplotlib.pyplot as plt
import argparse 
import numpy as np

def get_body_part_name(i):
    bodyparts = ["nose", ""]
    return bodyparts[i]

if __name__ == '__main__':
    # 导入包
    # 创建解析器
    parser = argparse.ArgumentParser() 

    #添加位置参数(positional arguments)
    parser.add_argument('--file', help='input a filename')
    args = parser.parse_args()
    print(args.file)
    f = open(args.file)
    line = f.readline()
    print(line)
    x = []
    ys = []
    xys = []
    i = 0
    while line:
        part = i % 25
        xyscore = line.split()
        xyscore[0] = float(xyscore[0])
        xyscore[1] = float(xyscore[1])
        xyscore[2] = float(xyscore[2])
        if part == 0:
            x.append(i)
        y = 1080 - float(xyscore[1])
        if len(ys) <= part:
            ys.append([y])
            xys.append([xyscore])
        else:
            ys[part].append(y)
            xys[part].append(xyscore)
        line = f.readline()
        i+=1
    f.close()
    ## python list -> np.array
    xy1s = np.array(xys[1])
    xy2s = np.array(xys[2])
    xy3s = np.array(xys[3])
    xy4s = np.array(xys[4])
    xy8s = np.array(xys[8])
    xy9s = np.array(xys[9])
    xy10s = np.array(xys[10])
    # 作图
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8,4))
    # 髋关节角度
    ma_x = xy1s[...,0] - xy8s[...,0]
    ma_y = xy1s[...,1] - xy8s[...,1]
    mb_x = xy8s[...,0] - xy10s[...,0]
    mb_y = xy8s[...,1] - xy10s[...,1]
    ab_x = xy10s[...,0] - xy1s[...,0]
    ab_y = xy10s[...,1] - xy1s[...,1]
    ab_val2 = ab_x * ab_x + ab_y * ab_y
    ma_val2 = ma_x * ma_x + ma_y * ma_y
    mb_val2 = mb_x * mb_x + mb_y * mb_y
    cos_M = (ma_val2+mb_val2-ab_val2) / (2 * np.sqrt(ma_val2)*np.sqrt(mb_val2))
    angleAMB = np.arccos(cos_M)/np.pi * 180
    ax1.scatter(np.array(x),angleAMB)
    ax1.set_title("hip joint angle")
    # 大臂和躯干的角度
    ma_x = xy2s[...,0] - xy3s[...,0]
    ma_y = xy2s[...,1] - xy3s[...,1]
    mb_x = xy2s[...,0] - xy9s[...,0]
    mb_y = xy2s[...,1] - xy9s[...,1]
    ab_x = xy3s[...,0] - xy9s[...,0]
    ab_y = xy3s[...,1] - xy9s[...,1]
    ab_val2 = ab_x * ab_x + ab_y * ab_y
    ma_val2 = ma_x * ma_x + ma_y * ma_y
    mb_val2 = mb_x * mb_x + mb_y * mb_y
    cos_M = (ma_val2+mb_val2-ab_val2) / (2 * np.sqrt(ma_val2)*np.sqrt(mb_val2))
    angleAMB = np.arccos(cos_M)/np.pi * 180
    ax2.scatter(np.array(x),angleAMB)
    ax2.set_title("should joint angle")
    # 大臂小臂角度
    ma_x = xy2s[...,0] - xy3s[...,0]
    ma_y = xy2s[...,1] - xy3s[...,1]
    mb_x = xy3s[...,0] - xy4s[...,0]
    mb_y = xy3s[...,1] - xy4s[...,1]
    ab_x = xy2s[...,0] - xy4s[...,0]
    ab_y = xy2s[...,1] - xy4s[...,1]
    ab_val2 = ab_x * ab_x + ab_y * ab_y
    ma_val2 = ma_x * ma_x + ma_y * ma_y
    mb_val2 = mb_x * mb_x + mb_y * mb_y
    cos_M = (ma_val2+mb_val2-ab_val2) / (2 * np.sqrt(ma_val2)*np.sqrt(mb_val2))
    angleAMB = np.arccos(cos_M)/np.pi * 180
    ax3.scatter(np.array(x),angleAMB)
    ax3.set_title("elbow joint angle")
    fig.tight_layout()
    plt.show()
