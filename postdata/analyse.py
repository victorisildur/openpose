import matplotlib.pyplot as plt
import argparse
import numpy as np
from matplotlib.widgets import CheckButtons
import file_reader
from angle_calc import *


def get_body_part_name(i):
    bodyparts = ["nose", ""]
    return bodyparts[i]


if __name__ == '__main__':
    # 导入包
    # 创建解析器
    parser = argparse.ArgumentParser()

    # 添加位置参数(positional arguments)
    parser.add_argument('--file', help='input a filename')
    args = parser.parse_args()
    filename = args.file
    print(filename)
    t, xys = file_reader.read_x_y_score_list(args.file)
    ## python list -> np.array
    xy1s = np.array(xys[1])
    xy2s = np.array(xys[2])
    xy3s = np.array(xys[3])
    xy4s = np.array(xys[4])
    xy8s = np.array(xys[8])
    xy9s = np.array(xys[9])
    xy10s = np.array(xys[10])
    xy11s = np.array(xys[11])
    xy22s = np.array(xys[22])
    # 髋关节角度
    hip_angle = calc_angle(xy1s, xy10s, xy9s)
    # 大臂和躯干的角度
    shoulder_angle = calc_angle(xy3s, xy9s, xy2s)
    # 大臂小臂角度
    elbow_angle = calc_angle(xy2s, xy4s, xy3s)
    # 膝盖角度
    knee_angle = calc_angle(xy9s, xy11s, xy10s)
    # 脚踝角度
    ankle_angle = calc_angle(xy10s, xy22s, xy11s)
    # 肩膀高度
    shoulder_height = np.subtract(720, xy2s[..., 1])
    # 手腕高度
    wrist_height = np.subtract(720, xy4s[..., 1])
    # 手腕x
    wrist_x = xy4s[..., 0]
    # 膝盖高度
    knee_height = np.subtract(720, xy10s[..., 1])
    # 手腕高度
    elbow_height = np.subtract(720, xy3s[..., 1])
    # 髋高
    hip_height = np.subtract(720, xy9s[..., 1])
    # 脚踝高度
    ankle_height = np.subtract(720, xy11s[..., 1])
    # 作图
    fig, ax = plt.subplots()
    plt.title(filename)
    l0, = ax.plot(t, shoulder_height, label='shoulder height')
    l1, = ax.plot(t, wrist_height, label='wrist height')
    l7, = ax.plot(t, hip_height, label='hip height')
    l6, = ax.plot(t, knee_height, label='knee height')
    l9, = ax.plot(t, elbow_height, label='elbow height')
    l11, = ax.plot(t, ankle_height, label='ankle height')
    l2, = ax.plot(t, hip_angle, label='hip angle', linestyle='dashed')
    l3, = ax.plot(t, shoulder_angle, label='shoulder angle', linestyle='dashed')
    l4, = ax.plot(t, elbow_angle, label='elbow angle', linestyle='dashed')
    l5, = ax.plot(t, knee_angle, label='knee angle', linestyle='dashed')
    l8, = ax.plot(t, wrist_x, label='wrist x', linestyle='dashdot')
    l10, = ax.plot(t, ankle_angle, label='ankle angle', linestyle='dashdot')
    l12, = ax.plot(t, knee_angle + hip_angle, label='knee + hip angle', linestyle='dashdot')
    lines = [l0, l1, l6, l7, l9, l11, l2, l3, l4, l5, l8, l10]
    ax.set_yticks(np.arange(0, 720, 50))
    plt.legend()
    plt.subplots_adjust(left=0.2)
    plt.grid(True)

    # Make checkbuttons with all plotted lines with correct visibility
    rax = plt.axes([0.05, 0.4, 0.1, 0.15])
    labels = [str(line.get_label()) for line in lines]
    visibility = [line.get_visible() for line in lines]
    check = CheckButtons(rax, labels, visibility)
    def func(label):
        index = labels.index(label)
        lines[index].set_visible(not lines[index].get_visible())
        plt.draw()
    check.on_clicked(func)

    plt.gcf().canvas.set_window_title(filename)
    plt.show()
