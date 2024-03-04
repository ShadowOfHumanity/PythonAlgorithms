def Fsequence(sequence):
    old = 0
    new = 1
    fibbonaci = 0
    for i in range(sequence):
        print(fibbonaci)
        fibbonaci = old + new
        old = new
        new = fibbonaci

term = 10
Fsequence(term)

