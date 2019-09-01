# for q-iteration
import math
  
def R(s1, a, s2):
    if s1 == 0 and s2 == 0:
        return 0.0
    elif s1 == s2:
        return 1.0/math.sqrt(s1 + 4)
    else:
        return abs(pow(s2 - s1, 1/3))

def T(s, a):
    if s == 0:
        return {0: 1}
    elif s in [1, 2, 3]:
        if a == 'M':
           return {s - 1: 1}
        else:
           return {s: 0.3, s+2: 0.7}
    else:
        if a == 'M':
           return {s-1: 1}
        else:
           return {s: 1}

def max_q(q_val, s):
    return max(q_val[s].values())

def q_iter(q0, gamma):
    q1 =[{"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0}]
    for s in range(6):
        for a in ['M', 'C']:
            t = T(s, a)
            q1[s][a] = 0.0
            for sn in t:
                q1[s][a] += t[sn]*(R(s,a,sn) + gamma*max_q(q0, sn))

    for i in range(len(q1)):
        print (i, q1[i], "pi*:", max(q1[i], key = lambda k: q1[i][k]), "v*:", max(q1[i].values()))
    return q1

if __name__ == '__main__':
    print("reward: 0 -> 0", R(0, 'M', 0))
    print("reward: 1 -> 3", R(1, 'M', 3))
    print("reward: 1 -> 0", R(1, 'M', 0))
    print("reward: 2 -> 1", R(2, 'M', 1))
    print("reward: 2 -> 2", R(2, 'M', 2))

    q0 =[{"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0},
         {"C":0.0, "M": 0.0}]

    q_iter(q0, 0.6)
