import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1",12000))

print ("UDP server is running and waiting for messages...")

while True:
    message, client_address = server_socket.recvfrom(2048)

    try:
        text = message.decode("utf-8")

    except UnicodeDecodeError:
        print("Error: Received invalid UTF-8 data")
        continue

    print("Message received:", text)

    if ":" in text:
        command, content = text.split(":",1)

        if command == "UPPER":
            response=content.upper()

        elif command == "LOWER":
            response=content.lower()

        elif command == "LENGTH":
            response=str(len(content))

        elif command == "REVERSE":
            response=content[::-1]


        else:
            response = "ERROR: Unkown command"

    else:
        response = "ERROR: Invalid message format"
        


    server_socket.sendto(response.encode("utf-8"),client_address)