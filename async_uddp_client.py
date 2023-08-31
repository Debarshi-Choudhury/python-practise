#!/usr/bin/python3

import asyncio

server_ip = "127.0.0.1"
server_port = 20001
responses = []

async def udp_request(key, loop):
    transport, _ = await loop.create_datagram_endpoint(
        lambda: MyProtocol(key),
        remote_addr=(server_ip, server_port)
    )
    await asyncio.sleep(0.1)  # Wait a bit for sending the request
    transport.sendto(f"GET {key}".encode())

class MyProtocol:
    def __init__(self, key):
        self.key = key
        # self.responses = responses

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        response = data.decode()
        print('data received: ', response)
        responses.append(f"Response for {self.key}: {response}")
        # self.transport.close()
    
    def connection_lost(self, exc):
        print(f"Connection lost for {self.key}")
        # Perform any cleanup tasks or additional handling here

async def main():
    input_file = "input.txt"
    output_file = "output.txt"
    loop = asyncio.get_event_loop()
    

    with open(input_file, "r") as file:
        keys = [line.strip() for line in file]

    tasks = [udp_request(key, loop) for key in keys]
    await asyncio.gather(*tasks)

    await asyncio.sleep(10)

    print("responses:", responses)

    with open(output_file, "w") as file:
        for response in responses:
            file.write(response + "\n")



if __name__ == "__main__":
    asyncio.run(main())
