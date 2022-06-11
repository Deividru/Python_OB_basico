

if __name__=="__main__":
    nlist = []

    #entrada = "España, portugal, valencia, madrid, portugal, catalunya, brasil, madrid"
    #app = entrada.split(",")
    #print(app)

    app = input("Introduce una lista de paises separados por comas").split(",")

    def mifuncion(x):

        if not nlist.__contains__(x):
            nlist.append(x)
            return True

        return False

    resultado = filter(mifuncion,app)

    print (list(resultado))
