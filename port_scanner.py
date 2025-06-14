import socket
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

progress_lock = Lock()
total_ports_scanned = 0

MAX_WORKERS = 500


def generate_port_chunks(port_range):
    port_start, port_end = map(int, port_range.split('-'))
    total_ports = port_end - port_start + 1
    chunk_size = max(1, total_ports // MAX_WORKERS)
    port_chunks = []

    for i in range(MAX_WORKERS):
        start = port_start + i * chunk_size
        end = min(port_start + (i + 1) * chunk_size - 1, port_end)
        if start > port_end:
            break
        port_chunks.append([start, end])

    return port_chunks


def scan(ip_address, port_chunk):
    global total_ports_scanned
    total = port_chunk[1] - port_chunk[0] + 1
    for port in range(port_chunk[0], port_chunk[1] + 1):
        try:
            scan_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan_socket.settimeout(0.5)
            scan_socket.connect((ip_address, port))
            print(f"[!] Port {port} is OPEN")
        except:
            pass
        finally:
            scan_socket.close()

        # Update and print progress
        with progress_lock:
            total_ports_scanned += 1
            print(f"\r[⏳] Ports scanned: {total_ports_scanned}", end="", flush=True)
def banner():
    print(""""                                                
               @@@@@@@@@                        
           @@@@@@@@@@@@@@@@@                    
        @@@@@@@@@@@@@@@@@@@@@@@                 
      @@@@@@@             @@@@@@@               
     @@@@@@                 @@@@@@              
    @@@@@@@@@ @@@@@  @@@   @@@@@@@@             
   @@@@@@@@@@ @@@@@ @@@@@ @@@@@@@@@@            
   @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@            
   @@@@ @@@@@@@@@@@@@@@@@@@@@@@ @@@@@           
   @@@@ @@@@@@@@@@@@@@@@@@@@@@@ @@@@@           
   @@@@ @@@@@@@@@@@@@@@@@@@@@@@ @@@@@           
   @@@@  @@@@@@@@@@@@@@@@@@@@@  @@@@            
   @@@@@   @@@@@@@@@@@@@@@@    @@@@@            
    @@@@@     @@@@@@@@@@      @@@@@             
     @@@@@@    @@@@@@@@@    @@@@@@              
      @@@@@@@             @@@@@@@@@@@           
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
           @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@      
                @@@@@@@       @@@@@@@@@@@@@@    
                               @@@@@@@@@@@@@@   
                                @@@@@@@@@@@@@@  
                                  @@@@@@@@@@@@  
                                    @@@@@@@@@   
                                      @@@@@     
                                                
                                RORT SCANNER                                                                  
                                                                                                  Author:R4Y""")



def main():
    banner()
    ip_address=str(input("What s the targets IP ADDRESS"))
    port_range=str(input("Enter a port range on this format <<start-end>> or type 0 to scann all ports"))
    if port_range=='0' :
        port_range='0-65535'
    port_chunks=generate_port_chunks(port_range)
    start_time=time.time()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor :
        executor.map(scan,[ip_address] * len(port_chunks),port_chunks)
    finish_time=time.time()
    print()
    start_port, end_port = map(int, port_range.split('-'))
    print(f"Scanned ports {start_port}-{end_port} in {finish_time - start_time:.2f} seconds.")
if __name__=='__main__':
    main()
