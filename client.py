import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(5)

server_address = ("127.0.0.1",12000)

message = input("Type your message: ")

try:
    client_socket.sendto(message.encode("utf-8"),server_address)

    response, address = client_socket.recvfrom(2048)

    print("Server response: ", response.decode("utf-8"))

except socket.timeout:
    print("Error: Server did not respond within 5 seconds")

except ConnectionRefusedError:
    print("Error: Server is not available")

finally:
    client_socket.close()