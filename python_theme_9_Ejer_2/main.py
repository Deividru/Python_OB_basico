from functools import reduce

if __name__=="__main__":
    nlist = [1,2,3,4,5,6,7,8]
    nlitspares = []

    def pares(x):
        if x % 2 == 0 :
            nlitspares.append(x)
            return True

        return False

    print(nlist)

    resultado = filter(pares, nlist)

    print(list(resultado))

    resultado = reduce(lambda x,y: x+y , nlitspares)

    print(resultado)
