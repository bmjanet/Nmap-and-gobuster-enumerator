# Python Nmap + Gobuster Automation Script

This script automates two stages of basic reconnaissance:
1. It runs a full Nmap scan (-A -T4 -p-) against a target IP, and
2. It automatically launches Gobuster to brute-force directories on the discovered HTTP service(s).

It is designed for quick enumeration during CTFs, pentesting labs, and general reconnaissance.

## Features
- Performs a full aggressive Nmap scan on all ports.
- Runs Gobuster with 25 threads using a predefined wordlist.
- Simple command-line usage (only requires a target IP).
- Error handling for missing tools.
- Requires almost no configuration.

## Requirements
Python Packages

This script uses the python-nmap module: ```python-nmap```

## External Tools Needed
You must have the following installed and available in your system PATH:
- Nmap
- Gobuster

## Usage
`python3 nmap_bust.py <IP Address>`

