# WebSocket Mock Server with CSV Data

This project simulates a WebSocket server that sends pre-defined data to connected clients based on timestamps. The data is loaded from a CSV file containing random timestamps and associated values, which are sent in real-time to the clients. 

This mock server is designed to correctly simulate broadcasting data with timestamps, enabling you to test various behaviors that require a WebSocket server.

Additionally, a script is included to generate a CSV file with random data, which serves as input for the server.

Warning: This mock WebSocket server uses self-signed certificates for TLS encryption. While it is suitable for testing and development purposes, it is not recommended for production environments. In a production setting, you should use valid, trusted certificates issued by a recognized Certificate Authority (CA). Additionally, be aware that using self-signed certificates may expose your system to potential security risks, including man-in-the-middle attacks. Please take appropriate precautions when handling sensitive data and consider securing your connections with proper authentication and encryption in production.

## Technologies Used
- **Python 3.x**
- **asyncio**: To handle asynchronous operations and real-time data simulation.
- **websockets**: For WebSocket server and client communication.
- **ssl**: For securing the WebSocket connection (WSS).
- **csv**: For reading and writing the data from and to a CSV file.
- **datetime**: For handling and manipulating timestamps.

## Project Overview

1. **WebSocket Mock Server**:
   The server listens for incoming WebSocket connections over a secure connection (WSS). Once a client connects, the server sends the data from the CSV file in real-time, based on the timestamp values. The data is sent as soon as the internal clock reaches the corresponding timestamp.

2. **WebSocket Client**:
   A simple client script is included, which connects to the server and receives the data being broadcast. The client keeps running and printing the received messages.

3. **CSV Data Generation**:
   A Python script generates a CSV file `random_data.csv` that contains random timestamps between January 1, 2025 (00:00:00) and 00:00:10 of the same day. Each timestamp is paired with a random string as its value.


## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/websocket-mock-server.git

2. Install dependencies: Navigate to the project folder and install the required Python packages:
   ```bash
   pip install -r requirements.txt

3. Generate the data (if necessary):
   ```bash
   python3 generate_csv.py
   
4. Generate the TSL certificates: This step generates a self-signed SSL certificate for the WebSocket server.
   ```bash
   openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
  
5. Set server parameters in websocket_mock.py: Adjust the parameters (like the port or certificate paths) in websocket_mock.py as needed
   
6. Run the server:
   ```bash
   python3 websocket_mock.py
   
7. Run the client:
   ```bash
   python3 websocket_client.py
