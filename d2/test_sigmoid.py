import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

w1 = 0.89
w2=-0.28
x1=-3
x2=-3


print("Punctul ", x1, ",", x2, ":" ,sigmoid(w1*x1+w2*x2)) # 0.88 

x1=3
print("Punctul ", x1, ",", x2, ":" ,sigmoid(w1*x1+w2*x2)) # 0.88 

x2=3
print("Punctul ", x1, ",", x2, ":" ,sigmoid(w1*x1+w2*x2)) # 0.88 

x1=-3
x2=3
print("Punctul ", x1, ",", x2, ":" ,sigmoid(w1*x1+w2*x2)) # 0.88 