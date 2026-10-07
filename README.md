# DoS Cybersecurity Attack Assignment

## Selected Attack

**Denial of Service (DoS)**

This project demonstrates a simple and controlled **Denial of Service (DoS) attack simulation** using Python socket programming.

The demonstration runs only on **localhost (`127.0.0.1`)** and is intended for an authorized classroom assignment.

---

## 1. What is DoS?

A **Denial of Service (DoS)** attack attempts to make a service unavailable or less responsive by sending excessive requests or traffic to the service.

In this simulation, repeated requests are sent to a local TCP server. The purpose is to demonstrate the basic idea of how repeated requests can create additional work for a server and potentially affect its availability.

The main security property affected by DoS is **Availability**.

---

## 2. What I Built

This project contains two Python programs:

### `server.py`

A simple TCP server that:

* Runs on `127.0.0.1`
* Listens on port `5000`
* Accepts incoming connections
* Receives requests
* Counts and displays received requests
* Sends a simple response to the requester

### `dos_attack.py`

A controlled DoS demonstration program that:

* Connects to the local server
* Sends repeated requests
* Sends a total of 30 requests
* Uses a small delay between requests
* Targets only `127.0.0.1`

---

## 3. How the Simulation Works

The basic communication is:

```text
DoS Demonstration Program
          |
          | Repeated Requests
          ↓
   Local TCP Server
   127.0.0.1:5000
```

The server continuously waits for incoming connections.

The DoS demonstration program repeatedly connects to the server and sends a request.

The server accepts and processes each request.

In this simple server, there is **no rate-limiting mechanism** to restrict how many requests can be sent within a specific period. Therefore, the demonstration program can repeatedly send requests, and the server continues processing them.

This demonstrates the basic mechanism behind a DoS attack.

---

## 4. Files

```text
DoS-Cybersecurity-Attack/
│
├── server.py
├── dos_attack.py
└── README.md
```

---

## 5. Requirements

* Python 3
* No external Python packages are required

---

## 6. How to Run the Simulation

### Step 1: Start the Server

Open a terminal in the project folder and run:

```bash
python server.py
```

The expected output is:

```text
DoS Demo Server
Listening on 127.0.0.1:5000
Waiting for connections...
```

Leave this terminal running.

---

### Step 2: Run the DoS Demonstration

Open a **second terminal** in the same project folder and run:

```bash
python dos_attack.py
```

The program will send **30 controlled requests** to:

```text
127.0.0.1:5000
```

The program will display the requests as they are sent.

---

### Step 3: Check the Server

Go back to the first terminal.
