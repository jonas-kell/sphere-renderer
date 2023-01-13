import math
import numpy as np

phi = (1 + math.sqrt(5)) / 2
a = math.sin(2 * math.pi * 18 / 360)
b = math.cos(2 * math.pi * 18 / 360)
c = math.cos(2 * math.pi * 36 / 360)
d = math.sin(2 * math.pi * 36 / 360)


theta = np.radians(-36)
c, s = np.cos(theta), np.sin(theta)
RotMat = np.array(((c, -s), (s, c)))


def turn_2d_clockwise_45_degree(point_2d):
    new_point = (point_2d[0] - a - c, point_2d[1])
    rotated = RotMat @ np.array(new_point)
    return (rotated[0], rotated[1])


# 3d-coordinates

AAA = (+1, +1, +1)
BBB = (+1, +1, -1)
CCC = (+1, -1, +1)
DDD = (+1, -1, -1)
EEE = (-1, +1, +1)
FFF = (-1, +1, -1)
GGG = (-1, -1, +1)
HHH = (-1, -1, -1)
III = (0, +1 / phi, +phi)
JJJ = (0, +1 / phi, -phi)
KKK = (0, -1 / phi, +phi)
LLL = (0, -1 / phi, -phi)
MMM = (+1 / phi, +phi, 0)
NNN = (+1 / phi, -phi, 0)
OOO = (-1 / phi, +phi, 0)
PPP = (-1 / phi, -phi, 0)
QQQ = (+phi, 0, +1 / phi)
RRR = (+phi, 0, -1 / phi)
SSS = (-phi, 0, +1 / phi)
TTT = (-phi, 0, -1 / phi)

# 2d-coordinates

A = turn_2d_clockwise_45_degree((a, 0))
B = turn_2d_clockwise_45_degree((2 * c - a, 0))
C = turn_2d_clockwise_45_degree((2 * c, b))
D = turn_2d_clockwise_45_degree((c, b + d))
E = turn_2d_clockwise_45_degree((0, b))
F = turn_2d_clockwise_45_degree((c - a, 2 * b + d))
G = turn_2d_clockwise_45_degree((a - c, 2 * b + d))
H = turn_2d_clockwise_45_degree((-c, b + d))
I = turn_2d_clockwise_45_degree((3 * c - 2 * a, b + d))
J = turn_2d_clockwise_45_degree((3 * c - a, 2 * b + d))
K = turn_2d_clockwise_45_degree((2 * c - a, 2 * b + 2 * d))
L = turn_2d_clockwise_45_degree((c, 3 * b + d))
M = turn_2d_clockwise_45_degree((0, 3 * b + 2 * d))
N = turn_2d_clockwise_45_degree((-c, 3 * b + d))
O = turn_2d_clockwise_45_degree((a - 2 * c, 2 * b + 2 * d))
P = turn_2d_clockwise_45_degree((a - 3 * c, 2 * b + d))
Q = turn_2d_clockwise_45_degree((2 * a - 3 * c, b + d))
R = turn_2d_clockwise_45_degree((-2 * c, b))
S = turn_2d_clockwise_45_degree((a - 2 * c, 0))
T = turn_2d_clockwise_45_degree((-a, 0))
AA = turn_2d_clockwise_45_degree((4 * c, 0 + b))
BB = turn_2d_clockwise_45_degree((6 * c - 2 * a, b))
CC = turn_2d_clockwise_45_degree((6 * c - a, 0))
DD = turn_2d_clockwise_45_degree((5 * c - a, -d))
EE = turn_2d_clockwise_45_degree((4 * c - a, 0))
FF = turn_2d_clockwise_45_degree((5 * c - 2 * a, -b - d))
GG = turn_2d_clockwise_45_degree((3 * c, -b - d))
HH = turn_2d_clockwise_45_degree((3 * c - a, -d))
II = turn_2d_clockwise_45_degree((7 * c - 3 * a, -d))
JJ = turn_2d_clockwise_45_degree((7 * c - 2 * a, -b - d))
KK = turn_2d_clockwise_45_degree((6 * c - 2 * a, -b - 2 * d))
LL = turn_2d_clockwise_45_degree((5 * c - a, -2 * b - d))
MM = turn_2d_clockwise_45_degree((4 * c - a, -2 * b - 2 * d))
NN = turn_2d_clockwise_45_degree((3 * c - a, -2 * b - d))
OO = turn_2d_clockwise_45_degree((2 * c, -b - 2 * d))
PP = turn_2d_clockwise_45_degree((c, -b - d))
QQ = turn_2d_clockwise_45_degree((c + a, -d))
TT = turn_2d_clockwise_45_degree((4 * c - 2 * a, b))

# mapping (first 2d then 3d)

mapping = [
    (A, RRR),
    (B, BBB),
    (C, MMM),
    (D, AAA),
    (E, QQQ),
    (F, III),
    (G, KKK),
    (H, CCC),
    (I, MMM),
    (J, OOO),
    (K, EEE),
    (L, EEE),
    (M, SSS),
    (N, GGG),
    (O, GGG),
    (P, PPP),
    (Q, NNN),
    (R, NNN),
    (S, DDD),
    (T, RRR),
    (AA, OOO),
    (BB, EEE),
    (CC, SSS),
    (DD, TTT),
    (EE, FFF),
    (FF, HHH),
    (GG, LLL),
    (HH, JJJ),
    (II, SSS),
    (JJ, GGG),
    (KK, PPP),
    (LL, PPP),
    (MM, NNN),
    (NN, DDD),
    (OO, DDD),
    (PP, RRR),
    (QQ, BBB),
    (TT, OOO),
]


def get_2d_to_3d(point_3d):
    for mapped in mapping:
        if mapped[1] == point_3d:
            return mapped[0]

    raise IndexError


def get_3d_to_2d(point_2d):
    for mapped in mapping:
        if mapped[0] == point_2d:
            return mapped[1]

    raise IndexError


pentagons = [  # only the 2d points
    (A, B, C, D, E),
    (D, I, J, K, F),
    (G, F, L, M, N),
    (Q, H, G, O, P),
    (S, T, E, H, R),
    (E, D, F, G, H),
    (AA, EE, DD, CC, BB),
    (C, B, HH, EE, TT),
    (HH, QQ, PP, OO, GG),
    (FF, GG, NN, MM, LL),
    (II, DD, FF, KK, JJ),
    (EE, HH, GG, FF, DD),
]


def get_2d_coordinates_of_pentagons():
    return pentagons


cache_3d = [
    AAA,
    BBB,
    CCC,
    DDD,
    EEE,
    FFF,
    GGG,
    HHH,
    III,
    JJJ,
    KKK,
    LLL,
    MMM,
    NNN,
    OOO,
    PPP,
    QQQ,
    RRR,
    SSS,
    TTT,
]


def get_3d_coordinates():
    return cache_3d


cache_2d = [
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I,
    J,
    K,
    L,
    M,
    N,
    O,
    P,
    Q,
    R,
    S,
    T,
    AA,
    BB,
    CC,
    DD,
    EE,
    FF,
    GG,
    HH,
    II,
    JJ,
    KK,
    LL,
    MM,
    NN,
    OO,
    PP,
    QQ,
    TT,
]


def get_2d_coordinates():
    return cache_2d
