!!! Currently under Development ,Phantom_toolbox v0.1.5 lite verison available for now ... :)<br/><br/>
Run the following command in command prompt to install required libraries ...<br>
`pip install -r requirements.txt`
### The tools are pretty slow for now but I am working on it and pretty soon the phantom will have concurrent threads ...


# Phantom_toolbox
<br/>
[V 0.1.1 ]had less functionality,and was too slow for heavy tasks ... Also used CLI Menu structure for instructions like target , ports type , etc.
<br/><br/>
[V 0.1.5] Uses argparse to give a whole menu in single line , more efficient with more recon tools
<br/><br/>
Phantom_toolbox is a powerful and extensible hacking toolbox designed to provide commonly used security and reconnaissance tools in one place. This menu-driven framework allows users to easily access various utilities . The toolbox is built with scalability in mind, ensuring that new features and tools can be added seamlessly in the future. 

# How to use
If you see recon.py , main.py , and phantom_tool directory ... They are of no use , left debris of old version.<br/>
For Recon , Network Mapping , Forensics or OSINT PHM_Recon.py is available , for help you can type:<br/>
`python3 PHM_Recon.py -h`

Example:
`>> Python3 PHM_Recon.py <target domain> <port range> <scan type> -wh -dir -sub` 

# Phantom Introduction

Phantom toolbox is divided in three parts...<br/><br/>

Phantom Toolbox<br/>
  |<br/>
  |--Phantom_recon<br/>
  |<br/>
  |--Phantom_ [Coming_Soon]<br/>
  |<br/>
  |--Phantom_ [Coming_Soon]<br/>



# Phantom Recon

Phantom Recon has various kinds of Recon , Network Mapping , Forensics , and OSINT tools ...

## [1] PORT SCANNER
 . Scan for common ports , custom range and all ports .<br/>
 . Different methods for scanning available for stealth or fast scans (TCP,UDP,SYN,ACK,FIN,Xmas,NULL).<br/>
 . Fast scanning using concurrent threads .<br/>
   There are three different ranges for port scanning.<br>
   `-pS` for Common port only scan<br>
   `-pC` for Custom port scan works with `-p` (port) to scan custom range eg: `-p 100-200`<br>
   `-pA` for all 65536 port scanning .<br>
   
### All scan ranges also need arg for type of scan .(Default TCP)
   There are 7 methods to do scan listed below and how to use ...<br>
   `-sT` for TCP Three way handshake scan.<br>
   `-sS` for SYN scan.(Under Development)<br>
   `-sA` for ACK scan.(Under Development)<br>
   `-sU` for UDP scan.(Under Development)<br>
   `-sF` for FIN scan.(Under Development)<br>
   `-sX` for Xmas scan.(Under Development)<br>
   `-sN` for NULL scan.(Under Development)<br>
   `-sP` to Ping host activity.(Under Development)<br>

 ## [2]Whois Lookup
  . Find the info about any domain .<br/>
  . Full whois lookup with raw data on your screen<br/>
    You can use `-wh` for whois lookup .<br>

## [3]Subdomain Enumeration
 . Find active subdomains .<br/>
 . Helpfull in finding any hidden subdomain that can be exploited<br/>
   You can use `-sub` for subdomin enumeration .<br>
   Default wordlist contains subdomains for many use cases with common ones accross many websites.<br>

## [4]Directory Enumeration
 . Finds the directory of any website using a wordlist<br/>
 . Wordlist contains directory names from various sources reliable for most of the scans ... <br/>
 . If you want to use custom wordlist, you will have to add the path manually.<br/>
   You can use `-dir` for directory enumeration.<br>
