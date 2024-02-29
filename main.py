import socket, sys

if __name__ == "__main__":


    if len(sys.argv) >= 2:
        host = sys.argv[1]
    else: 
        host = input("Qual o host que deseja escanear")

    if len(sys.argv) >= 3:
        port1_str  = sys.argv[2]
    else:
        port1_str = input("Qual o port você deseja escanear?")


    #Análise via range
    if len(sys.argv) == 4:
        port2_str = sys.argv[3]
        
        try:
            port1 = int(port1_str)
        except:
            print("input invalido para o primeiro port")
            exit(1)

        try:
            port2 = int(port2_str)
        except:
            print("input invalido para o segundo port")
            exit(1)


        for port in range(port1, port2):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    if s.connect_ex((host, port)) == 0:
                        print(f"port {port} is open", end = "")
                        try:
                            print(f"-- {s.socket.getservbyport(port, 'tcp')}")
                        except:
                            print("")
            except Exception as err:
                print(err)
