import math

phi = (1 + math.sqrt(5)) / 2
a = math.sin(2 * math.pi * 18 / 360)
b = math.cos(2 * math.pi * 18 / 360)
c = math.cos(2 * math.pi * 36 / 360)
d = math.sin(2 * math.pi * 36 / 360)

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

A = (a, 0)
B = (2 * c - a, 0)
C = (2 * c, b)
D = (c, b + d)
E = (0, b)
F = (c - a, 2 * b + d)
G = (a - c, 2 * b + d)
H = (-c, b + d)
I = (3 * c - 2 * a, b + d)
J = (3 * c - a, 2 * b + d)
K = (2 * c - a, 2 * b + 2 * d)
L = (c, 3 * b + d)
M = (0, 3 * b + 2 * d)
N = (-c, 3 * b + d)
O = (a - 2 * c, 2 * b + 2 * d)
P = (a - 3 * c, 2 * b + d)
Q = (2 * a - 3 * c, b + d)
R = (-2 * c, b)
S = (a - 2 * c, 0)
T = (-a, 0)
AA = (4 * c, 0 + b)
BB = (6 * c - 2 * a, b)
CC = (6 * c - a, 0)
DD = (5 * c - a, -d)
EE = (4 * c - a, 0)
FF = (5 * c - 2 * a, -b - d)
GG = (3 * c, -b - d)
HH = (3 * c - a, -d)
II = (7 * c - 3 * a, -d)
JJ = (7 * c - 2 * a, -b - d)
KK = (6 * c - 2 * a, -b - 2 * d)
LL = (5 * c - a, -2 * b - d)
MM = (4 * c - a, -2 * b - 2 * d)
NN = (3 * c - a, -2 * b - d)
OO = (2 * c, -b - 2 * d)
PP = (c, -b - d)
QQ = (c + a, -d)
TT = (4 * c - 2 * a, b)

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


def get_3d_coordinates():
    return [
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


def get_2d_coordinates():
    return [
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
