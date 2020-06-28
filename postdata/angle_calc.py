import numpy as np
#已知点A,B,C, 求∠C
def calc_angle(A, B, C):
    AC_dx = A[..., 0] - C[..., 0]
    AC_dy = A[..., 1] - C[..., 1]
    BC_dx = B[..., 0] - C[..., 0]
    BC_dy = B[..., 1] - C[..., 1]
    AB_dx = A[..., 0] - B[..., 0]
    AB_dy = A[..., 1] - B[..., 1]
    c2 = AB_dx * AB_dx + AB_dy * AB_dy
    b2 = AC_dx * AC_dx + AC_dy * AC_dy
    a2 = BC_dx * BC_dx + BC_dy * BC_dy
    cos_C = (b2 + a2 - c2) / (2 * np.sqrt(b2) * np.sqrt(a2))
    angle_C = np.arccos(cos_C) / np.pi * 180
    return angle_C
