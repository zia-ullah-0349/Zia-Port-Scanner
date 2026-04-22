import socket

print("=== PORT SCANNER ===")
target = input("Enter target Ip: ")

print("Scanning Ports 1 to 100 ... ")
for port in range(1, 101):
    s = socket.socket()
    s.settimeout(1)

    try:
        s.connect((target,port))
        print(f"Port {port} is OPEN! ")
    except:
        pass    # Didn't want to see closed Ports
    s.close()
print("Scan COMPLETED! ")