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

## Extra
If you want to run the program on your path so it is always available (like nmap), do this:
1. Give the program executable priviledges
    `sudo chmod +x nmap_bust.py`
2. Move/copy the program to your local bin, give it a unique name so you don't have to type those pesky periods.
    `sudo cp nmap_bust.py /usr/local/bin/nmapbuster`
3. Give the program unix lettering
    `sudo dos2unix /usr/local/bin/nmapbust`
4. Run it!
    `nmapbuster 127.0.0.1`
