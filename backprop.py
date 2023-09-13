import numpy as np

x=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
x=x/np.amax(x,axis=0)
y=y/100

def sigmoid(z):
    return 1/(1+np.exp(-z))

def der_sigmoid(z):
    return z*(1-z)
inp_l = 2
hid_l=3
out_l=1

wh = np.random.uniform(size=(inp_l,hid_l))
bh= np.random.uniform(size=(1,hid_l))
wout = np.random.uniform(size=(hid_l,out_l))
bout = np.random.uniform(size=(1,out_l))

epoch=5
lr=0.1

for i in range(epoch):
    hinp1=np.dot(x,wh)
    hinp=hinp1 + bh
    h_act = sigmoid(hinp)

    out1=np.dot(h_act,wout)
    out = out1+bout
    output = sigmoid(out)

    eo = y-output
    outgrad = der_sigmoid(output)
    d_out = eo*outgrad

    eh = d_out.dot(wout.T)
    hidngrad = der_sigmoid(h_act)
    d_h = eh*hidngrad

    wout += h_act.T.dot(d_out)*lr
    wh += x.T.dot(d_h)*lr
    bout += np.sum(d_out,axis=0,keepdims=True)*lr
    bh += np.sum(d_h,axis=0,keepdims=True)*lr


print(x)
print(y)
print(output)
