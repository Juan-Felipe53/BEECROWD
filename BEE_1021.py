import math as mt
billetes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
x = round(float(input()),2)
total = x
while x > 0:
    for i in range(len(billetes)):
        v = x/billetes[i]
        count = 0
        if(billetes[i]==100):
            print("NOTAS:")
        elif(billetes[i]==1):
            print("MOEDAS:")
        if v >= 1:
            if billetes[i]>=2:
                count = float(billetes[i])*mt.floor(v)
                print(f"{mt.floor(v)} nota(s) de R$ {billetes[i]:.2f}")
            elif billetes[i]<2:
                count = float(billetes[i])*mt.floor(v)
                print(f"{mt.floor(v)} moeda(s) de R$ {billetes[i]:.2f}")
            x = round(x - count,2) 

            
        elif v<1:
            if billetes[i]>=2:
                print(f"0 nota(s) de R$ {billetes[i]:.2f}")
            elif billetes[i]<2:
                print(f"0 moeda(s) de R$ {billetes[i]:.2f}")
    
    