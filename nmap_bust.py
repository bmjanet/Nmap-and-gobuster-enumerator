#!/usr/bin/env python3

import nmap
import subprocess
import sys

def run_gobuster(targetUrl, wordlistPath):
    print(f"[+] Starting GoBuster on {targetUrl} with wordlist {wordlistPath}")
    try:
        command = ['gobuster', 'dir', '-u', targetUrl, '-w', wordlistPath, '-t', '50']
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False, timeout=300)
        print("[+] GoBuster Scan Results:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except FileNotFoundError:
        print("Error: GoBuster is not installed or not found in PATH.")



def run_nmap(targetIp):
    nm = nmap.PortScanner()
    print(f"[+] Starting Nmap Scan on {targetIp}")
    nm.scan(hosts=targetIp, arguments='-A -T4 -p-')

    print(f"[+] Nmap Scan Results for {targetIp}:")
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f"Port: {port}\tState: {state}\tService: {service}")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        targetIp = sys.argv[1]
    else:
        print("No target IP Provided.")
        print("Usage: python3 script.py <target_ip>")
        sys.exit(1)

    print(f'-'*10 + f"[+] Target IP: {targetIp}" + f'-'*10)

    targetUrl = "http://" + targetIp
    wordlistPath = "/usr/share/wordlists/dirb/big.txt"
    
    # ----------------------
    run_nmap(targetIp)
    print("\n" + "-"*40 + "\n")

    run_gobuster(targetUrl, wordlistPath)
