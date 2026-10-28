# UDP Client-Server Application

A simple UDP client-server application written in Python.

This project demonstrates basic socket programming, UDP communication, command processing, and error handling.

## Features

- UDP communication using Python sockets
- Text processing commands
- Client-side timeout handling
- Error handling for invalid UTF-8 messages
- Basic input validation

## Supported Commands

| Command | Example | Response |
|---------|---------|----------|
| UPPER | `UPPER:hello` | `HELLO` |
| LOWER | `LOWER:HELLO` | `hello` |
| LENGTH | `LENGTH:hello` | `5` |
| REVERSE | `REVERSE:hello` | `olleh` |

## Requirements

- Python 3
- No external Python libraries required

## How to Run

Open a terminal and start the server:

```bash
python3 server.py
```

Open another terminal and start the client:

```bash
python3 client.py
```

Enter a command, for example:

```text
UPPER:hello world
```

Expected response:

```text
HELLO WORLD
```

## Network Configuration

- Protocol: UDP
- IP address: `127.0.0.1`
- Server port: `12000`

The application currently runs locally using the loopback interface.

## What I Learned

- TCP vs. UDP communication
- Socket programming in Python
- IP addresses and port numbers
- Encoding and decoding data
- Exception handling
- Input validation
- Git version control

## Future Improvements

- Better command validation
- Logging
- Automated tests
- Support for additional commands