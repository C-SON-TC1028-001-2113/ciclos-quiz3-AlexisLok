def main():
    #escribe tu código abajo de esta línea
    n=int(input(""))
    i=0
    con = 0
    while i < n:
        x = float(input(""))
        con = con + x
        i += 1
    print (con/n)

if __name__=='__main__':
    main()
