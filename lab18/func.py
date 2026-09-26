def med(n):
    
    return sum(n) / len(n)
 
 
def qtd_med(n, m):
    
    q = 0
    for x in n:
        if x >= m:
            q += 1
    return q
 
 
def sep(n):
    
    par = []
    imp = []
 
    for i in range(len(n)):
        if i % 2 == 0:
            par = par + [n[i]]
        else:
            imp = imp + [n[i]]
 
    return par, imp
 
 
def est(n):

    t = len(n)
    ap = 0
    rec = 0
    rep = 0
 
    for x in n:
        if x >= 7.0:
            ap += 1
        elif x >= 5.0:
            rec += 1
        else:
            rep += 1
 
    pa = (ap / t) * 100
    pr = (rec / t) * 100
    pv = (rep / t) * 100
 
    return pa, pr, pv
 
 
def maior(n, nom):
   
    mx = max(n)
    i = n.index(mx)
    a = nom[i]
    return mx, a
 
 
def conc(n):
    
    c = []
    for x in n:
        if x >= 9.0:
            c = c + ["A"]
        elif x >= 7.0:
            c = c + ["B"]
        elif x >= 5.0:
            c = c + ["C"]
        else:
            c = c + ["D"]
    return c