# DoS Cybersecurity Attack Assignment

Selected attack: Denial of Service (DoS)

## Files
- server.py - localhost TCP server
- dos_attack.py - controlled localhost-only DoS demonstration
- README.md - instructions and video guide

## Requirements
Python 3. No external packages are required.

## Test process

### 1. Open the folder
Extract the ZIP and open this folder in VS Code.

### 2. Check Python
Open a terminal:
    python --version

### 3. Start the server
Terminal 1:
    python server.py

Expected:
    DoS Demo Server
    Listening on 127.0.0.1:5000
    Waiting for connections...

Leave it running.

### 4. Run the attack
Open Terminal 2:
    python dos_attack.py

It will send 30 controlled requests to 127.0.0.1.

### 5. Check the server
Terminal 1 will show:
    Request #1 received...
    Request #2 received...
    ...
This demonstrates repeated requests arriving at the service.

### 6. Stop the server
Press Ctrl+C in Terminal 1.

## Video order
1. Introduce Denial of Service.
2. Show server.py.
3. Start the server.
4. Explain that the server is ready for normal requests.
5. Show dos_attack.py.
6. Run the attack.
7. Show the many requests in Terminal 1.
8. Explain that availability is the affected security property.
9. Explain that lack of rate limiting/connection controls makes repeated requests possible.
10. Explain defenses: rate limiting, connection limits, filtering, monitoring, firewalls, and DDoS protection.
11. Conclude.

## Suggested simple script
"My selected attack is Denial of Service, or DoS. It attempts to make a service unavailable or less responsive by sending excessive requests."

"I created a simple Python TCP server that listens on localhost port 5000 and counts incoming connections."

"Now I run my controlled attack program. It sends 30 rapid requests to my own localhost server."

"As we can see, the server receives many requests in a short period. This demonstrates how repeated requests can put additional load on a service."

"The main security property affected is availability."

"Possible defenses include rate limiting, connection limits, request filtering, monitoring, firewalls, and DDoS protection."

"All traffic in this demonstration targets 127.0.0.1, my own computer."

## Important
Use only 127.0.0.1 for this classroom demonstration. Do not change the target to another computer, website, public IP, or server.

## Submission
Upload server.py and dos_attack.py to GitHub and submit the repository link in the private Google Classroom comments, as required by the assignment.
