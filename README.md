# Port Scanner

Port Scanner is a lightweight Python tool designed to scan and identify open ports on a target system. It helps in assessing the security posture of a network by detecting open ports that could be potential entry points for unauthorized access.

# Features:
TCP Port Scanning: Identifies open TCP ports on the target system.
User-Friendly Interface: Simple command-line interface for ease of use.
Customizable Range: Allows users to specify a range of ports to scan.
Fast Execution: Optimized for quick scanning of ports.

# Installation

1. Clone the repository:
   ```
   git clone https://github.com/RizwanHaq11/PROJECT-1.git
    cd PROJECT-1

   ```

2. Install required dependencies:

   ```
    pip install -r requirements.txt

   ```

# Usage

1. Run the port scanner:
   ```
      python scan.py <target_ip> <start_port> <end_port>

   ```
2. Example:

   ```
     python scan.py 192.168.1.1 20 1024

   ```
