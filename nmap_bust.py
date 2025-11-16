#!/usr/bin/env python3

import nmap
import subprocess
import sys
import argparse

def run_gobuster(targetUrl, httpPorts, wordlistPath):
    print(f"[+] Starting GoBuster on {targetUrl} with wordlist {wordlistPath}")
    try:
        for port in httpPorts:
            command = ['gobuster', 'dir', '-u', f"{targetUrl}:{port}", '-w', wordlistPath, '-t', '50']
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
            print("[+] GoBuster Scan Results:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except FileNotFoundError:
        print("Error: GoBuster is not installed or not found in PATH.")



def run_nmap(targetIp):
    try:
        nm = nmap.PortScanner()
        print(f"[+] Starting Nmap Scan on {targetIp}")
        nm.scan(hosts=targetIp, arguments='-A -T4 -p-')

        httpPorts = []

        print(f"[+] Nmap Scan Results for {targetIp}:")
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    data = nm[host][proto][port]
                    state = data['state']
                    service = data.get('name', '')
                    if service in ['http', 'https']:
                        httpPorts.append(port)
                    version = data.get('version', '')
                    product = data.get('product', '')
                    extrainfo = data.get('extrainfo', '')

                    print(f"Port: {port}\tState: {state}\tService: {service}\t"
                        f"Product: {product}\tVersion: {version}\tExtra: {extrainfo}")
        print(f"[+] HTTP/HTTPS Ports Found: {httpPorts}")
        return httpPorts
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting cleanly...")
        sys.exit(1)
    



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
    httpPorts = run_nmap(targetIp)
    print("\n" + "-"*40 + "\n")

    run_gobuster(targetUrl, httpPorts, wordlistPath)

