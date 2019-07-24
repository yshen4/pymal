import numpy as np

def sigmoid(x):
    if x >= 50:
        return 1
    elif x <= -50:
        return 0
    else:
        return 1.0/(1.0+np.exp(-x))

def cal_gate(Wh, h, Wx, x, b):
    z = Wh*h + Wx * x + b
    return sigmoid(z)

def cal_mem(ft, ct, it, wch, h, wcx, x, bc):
    v = wch*h + wcx*x + bc
    if v <= -50:
       tanhv = -1
    else:
       tanhv = np.tanh(v)
    return ft * ct + it*tanhv

def cal_visiblestate(ot, ct):
    return ot * np.tanh(ct)

if __name__ == '__main__':
    '''
    print('sigmoid(-2)=', sigmoid(-2))
    print('sigmoid(-1)=', sigmoid(-1))
    print('sigmoid(0)=', sigmoid(0))
    print('sigmoid(1)=', sigmoid(1))
    print('sigmoid(2)=', sigmoid(2))
    '''
    #X = [0, 0, 1, 1, 1, 0]
    X = [1, 1, 0, 1, 1]
    ht = 0
    ct = 0

    # forget gate
    wfh = 0
    wfx = 0
    bf = -100
    
    # input gate
    wih = 0
    wix = 100
    bi = 100

    # ouput gate
    woh = 0
    wox = 100
    bo = 0

    # ouput gate
    wch = -100
    wcx = 50
    bc = 0

    for x in X:
        ft = cal_gate(wfh, ht, wfx, x, bf)
        it = cal_gate(wih, ht, wix, x, bi)
        ot = cal_gate(woh, ht, wox, x, bo)

        ct = cal_mem(ft, ct, it, wch, ht, wcx, x, bc)
        ht = cal_visiblestate(ot, ct)
        ht = np.rint(ht)

        #print(ft, it, ot, ct, ht)
        print(ht)
