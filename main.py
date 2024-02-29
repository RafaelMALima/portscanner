import socket, sys

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if len(sys.argv) >= 2:
        host = sys.argv[1]
    else: 
        host = input("Qual o host que deseja escanear")

    if len(sys.argv) >= 3:
        port1  = sys.argv[2]
    else:
        port1 = input("Qual o port você deseja escanear?")


    #Análise via range
    if len(sys.argv) == 4:
        port2 = sys.argv[3]
        
        try:
            port1 = int(port1)
        except:
            print("input invalido para o primeiro port")
            exit(1)
        try:
            port2 = int(port2)
        except:
            print("input invalido para o segundo port")
            exit(1)


        for port in range(port1, port2):
            connection = s.connect_ex((host,port))
            if connection == 0:
                print(f"port {port} is open", end = "")
                try:
                    print("--", socket.getservbyport(port, ''))
                except:
                    print("")


