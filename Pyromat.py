import pyromat as pm

r22 = pm.get('ig.CHClF2')
h = r22.s(p=100000, T=298.15)
print(h)
