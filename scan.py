import nmap

scanner = nmap.PortScanner()

print("Welcome to port scanner!!")
print("---------------------------------------------")


ip_addr = input("Please enter the IP Address to scan: ")
print("The IP entered is ",ip_addr)
type(ip_addr)

resp  = input(""" \n Please enter the type of scan you want to run:
              1)SYN-ACK SCAN
              2)UDP SCAN
              3)Comprehensive Scan \n""")

print("You have selected option: ",resp)

if resp == '1':
  print("###SYN ACK SCAN###")
  print("Nmap Version: ",scanner.nmap_version())
  scanner.scan(ip_addr,'1-1024','-v -sS')
  print(scanner.scaninfo())
  print("(*)Ip Status: ",scanner(ip_addr).state())
  print(scanner[ip_addr].all_protocols())
  print("($) Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
  print("###UDP SCAN###")
  print("Nmap Version: ",scanner.nmap_version())
  scanner.scan(ip_addr,'1-1024','-v -sU')
  print(scanner.scaninfo())
  print("(*)Ip Status: ",scanner(ip_addr).state())
  print(scanner[ip_addr].all_protocols())
  print("($) Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
  print("###COMPREHENSIVE SCAN###")
  print("Nmap Version: ",scanner.nmap_version())
  scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')
  print(scanner.scaninfo())
  print("(*)Ip Status: ",scanner(ip_addr).state())
  print(scanner[ip_addr].all_protocols())
  print("($) Open Ports: ", scanner[ip_addr]['tcp'].keys())

else:
  print("Please enter a valid option")