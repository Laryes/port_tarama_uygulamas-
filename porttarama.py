import socket 
from concurrent.futures import ThreadPoolExecutor

def port_tarama(ip,port):

    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect(ip,port)
            print(f"[+] Port {port} açık")
    except:
        pass  
def main():
    print("Port Tarayıcı")
    ip = input("Hedef IP veya Alan Adı: ")
    start_port = int(input("Başlangıç portunu girin: "))
    end_port = int(input("Bitiş portunu girin: "))

    print(f"{ip} adresinde portlar taranıyor...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port,end_port +1):
            executor.submit(port_tarama, ip, port)

if __name__ == "__main__":
    main()


