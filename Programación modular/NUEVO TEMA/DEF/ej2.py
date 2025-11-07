def esMultiplo(num1,num2):
    esMultiplo = num1 % num2 == 0
    return esMultiplo

es = esMultiplo(6,2)  #print(esMultiplo(6,2))
if es:
    print("Son múltiplos")
