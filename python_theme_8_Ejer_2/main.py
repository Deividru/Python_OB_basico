

def main():
    f= open("newdoc.txt","w")

    f.write("mi primera linea en Txt\n")
    f.write("mi segunda linea\n")

    print("documenTo creado y linea insertada\n")

    f= open("newdoc.txt", "r")

    datos = f.read()

    print (datos)

    f.close()

if __name__ == "__main__":
    main()


