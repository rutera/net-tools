import urllib2
from urllib2 import urlopen, Request, URLError, HTTPError
import urllib
import json
import os
import socket
import sys

print 80 * "*"
print 28 * " " , "RUTERA NET-TOOLS Toolkit" , 28 * " "
print 80 * "*"
def print_menu():       
    print 37 * "-" , "MENU" , 37 * "-"
    print "1. HTTP HEADER LOOKUP"
    print "2. DNS LOOKUP"
    print "3. PORT SCANNER"
    print "4. IP Geo Location"
    print "5. Zone Transfer Check"
    print "6. Whois Lookup"
    print "7. Find Shared DNS shared"
    print "8. Reverse DNS Lookup"
    print "9. Reverse IP Lookup"
    print "10. Ping Check"
    print "11. Trace Route"
    print "12. Exit"
    print 80 * "-"

loop=True     
 
while loop:          
    print_menu()    
    choice = input("Enter your choice [1-12]: ")
    
    if choice==1:
        url = raw_input("Please Enter the Website to grab HTTP Header:  ")
        print " FOOTPRINTING TARGET "
        webUrl = urllib2.urlopen("https://api.hackertarget.com/httpheaders/?q=" + url)
  
        
        data = webUrl.read()
        print data

        
    elif choice==2:
        website = raw_input("Please Enter the Website for DNS Lookup:  ")
        print " DNS Lookup started "
        webUrl = urllib2.urlopen("https://api.hackertarget.com/dnslookup/?q=" + website)
  
        
        data = webUrl.read()
        print data
        
        
    elif choice==3:
        def get(url, decoding='utf-8'):
            return urlopen(url).read().decode(decoding)
        domain = raw_input("Please Enter IP or website to perform TCP port scan:   ")
        print " Scanning started Please wait "
        port = "http://api.hackertarget.com/nmap/?q=" + domain
        eliment = get(port)
        print(eliment)


        
    elif choice==4:
        
        website = raw_input("Please Enter Address Website or IP to perform Geolocation Lookup:   ")
        print " IP/Domain Geolocator has been started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/geoip/?q=" + website)
  
        
        data = webUrl.read()
        print data

        
    elif choice==5:
        website = raw_input("Please Enter Address Website to check DNS zone Transfer Example: xyz.com:   ")
        print " Dns zone Transfer started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/zonetransfer/?q=" + website)
  
        
        data = webUrl.read()
        print data
        
  
        
    elif choice==6:
        website = raw_input("Please Enter Address Website or IP to perform whois lookup:   ")
        print " WhoisLookup started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/whois/?q=" + website)
  
        
        data = webUrl.read()
        print data
    elif choice==7:
        website = raw_input("Please Enter the domain to check Shared or dedicated DNS servers Example: ns1.example.com:  ")
        print " Shared or Dedicated DNS Lookup started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/findshareddns/?q=" + website)
  
        
        data = webUrl.read()
        print data

    elif choice==8:
        website = raw_input("Please Enter the IP or Domain to Check Reverse dns Lookup:   ")
        print " Reverse DNS Lookup started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/reversedns/?q=" + website)
  
      
        data = webUrl.read()
        print data    
    elif choice==9:
        website = raw_input("Please Enter the IP Address or Domain:  ")
        print " Reverse IP Lookup started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/reverseiplookup/?q=" + website)
  
        
        data = webUrl.read()
        print data
    elif choice==10:
        website = raw_input("Please Enter the IP or domain to perform Ping Test:   ")
        print " Ping test started"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/nping/?q=" + website)
  
        
        data = webUrl.read()
        print data
    elif choice==11:
        website = raw_input("Enter Address Website to perform Traceroute:   ")
        print " Tracing route"
        webUrl = urllib2.urlopen("https://api.hackertarget.com/mtr/?q=" + website)
  
        
        data = webUrl.read()
        print data    
     
    elif choice==12:
	sys.exit("Bay")

        loop=False 
    else:
        
        raw_input("Wrong option selection. Enter any key to try again..")
