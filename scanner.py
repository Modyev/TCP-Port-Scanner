import socket
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time

colorama_init()

top_500_ports = {80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080,1723,111,995,993,5900,1025,587,8888,199,1720,465,548,113,81,6001,10000,514,5060,179,1026,2000,8443,8000,32768,554,26,1433,49152,2001,515,8008,49154,1027,5666,646,5000,5631,631,49153,8081,2049,88,79,5800,106,2121,1110,49155,6000,513,990,5357,427,49156,543,544,5101,144,7,389,8009,3128,444,9999,5009,7070,5190,3000,5432,1900,3986,13,1029,9,5051,6646,49157,1028,873,1755,2717,4899,9100,119,37,1000,3001,5001,82,10010,1030,9090,2107,1024,2103,6004,1801,5050,19,8031,1041,255,1049,1048,2967,1053,3703,1056,1065,1064,1054,17,808,3689,1031,1044,1071,5901,100,9102,8010,2869,1039,5120,4001,9000,2105,636,1038,2601,1,7000,1066,1069,625,311,280,254,4000,1993,1761,5003,2002,2005,1998,1032,1050,6112,3690,1521,2161,6002,1080,2401,4045,902,7937,787,1058,2383,32771,1033,1040,1059,50000,5555,10001,1494,593,2301,3,1,3268,7938,1234,1022,1074,8002,1036,1035,9001,1037,464,497,1935,6666,2003,6543,1352,24,3269,1111,407,500,20,2006,3260,15000,1218,1034,4444,264,2004,33,1042,42510,999,3052,1023,1068,222,7100,888,4827,1999,563,1717,2008,992,32770,32772,7001,8082,2007,740,5550,2009,5801,1043,512,2701,7019,50001,1700,4662,2065,2010,42,9535,2602,3333,161,5100,5002,2604,4002,6059,1047,8192,8193,2702,6789,9595,1051,9594,9593,16993,16992,5226,5225,32769,3283,1052,8194,1055,1062,9415,8701,8652,8651,8089,65389,65000,64680,64623,55600,55555,52869,35500,33354,23502,20828,1311,1060,4443,730,731,709,1067,13782,5902,366,9050,1002,85,5500,5431,1864,1863,8085,51103,49999,45100,10243,49,3495,6667,90,475,27000,1503,6881,1500,8021,340,78,5566,8088,2222,9071,8899,6005,9876,1501,5102,32774,32773,9101,5679,163,648,146,1666,901,83,9207,8001,8083,5004,3476,8084,5214,14238,12345,912,30,2605,2030,6,541,8007,3005,4,1248,2500,880,306,4242,1097,9009,2525,1086,1088,8291,52822,6101,900,7200,2809,395,800,32775,12000,1083,211,987,705,20005,711,13783,6969,3071,5269,5222,1085,1046,5987,5989,5988,2190,11967,8600,3766,7627,8087,30000,9010,7741,14000,3367,1099,1098,3031,2718,6580,15002,4129,6901,3827,3580,2144,9900,8181,3801,1718,2811,9080,2135,1045,2399,3017,10002,1148,9002,8873,2875,9011,5718,8086,3998,2607,11110,4126,5911,5910,9618,2381,1096,3300,3351,1073,8333,3784,5633,15660,6123,3211,1078,3659,3551,2260,2160,2100,16001,3325,3323,1104,9968,9503,9502,9485,9290,9220,8994,8649,8222,7911,7625,7106,65129,63331,6156,6129,60020,5962,5961,5960,5959,5925,5877,5825,5810,58080,57294,50800}
#print(len(top_500_ports))
top_100_ports = {80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080,1723,111,995,993,5900,1025,587,8888,199,1720,465,548,113,81,6001,10000,514,5060,179,1026,2000,8443,8000,32768,554,26,1433,49152,2001,515,8008,49154,1027,5666,646,5000,5631,631,49153,8081,2049,88,79,5800,106,2121,1110,49155,6000,513,990,5357,427,49156,543,544,5101,144,7,389,8009,3128,444,9999,5009,7070,5190,3000,5432,1900,3986,13,1029,9,5051,6646,49157,1028,873,1755,4899,9100,119,37,1000}
#print(len(top_100_ports))

Top500Ports = sorted(list(top_500_ports))
Top100Ports = sorted(list(top_100_ports))

openCount = 0
closedCount = 0

def scanner(ip, port, timeout):
    socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketObj.settimeout(timeout)
    resp = socketObj.connect_ex((ip,port))
    
    if resp == 0:
        print(f"{Fore.GREEN}Port {port} is Open!{Fore.WHITE}")
        socketObj.close()
        return True
    else:
        print(f"{Fore.RED}Port {port} is Closed{Fore.WHITE}")
        socketObj.close()
        return False


    

print(f'{Fore.WHITE}({Fore.RED}1{Fore.WHITE}) {Fore.RED}Scan a Specific Port{Style.RESET_ALL}')
print(f'{Fore.WHITE}({Fore.RED}2{Fore.WHITE}) {Fore.RED}Scan Top 100 Ports{Style.RESET_ALL}')
print(f'{Fore.WHITE}({Fore.RED}3{Fore.WHITE}) {Fore.RED}Scan Top 500 Ports{Style.RESET_ALL}')
print(f'{Fore.WHITE}({Fore.RED}4{Fore.WHITE}) {Fore.RED}Scan Custom Amount of Ports{Style.RESET_ALL}')
choice = int(input(f"{Fore.CYAN}\nInput your choice: {Fore.WHITE} "))
timeout = 0.5

start = None


if choice == 1:
    ip = input("What is the ip you want to scan its ports?\n")
    port = input("Which port you wanna scan on the ip " + ip + "\n")
    
    start = time.time()
    if scanner(str(ip),int(port),timeout) == True:
        openCount +=1
    else:
        closedCount +=1
        

elif choice == 2:
    ip = input("What is the ip you want to scan: ")
    
    start = time.time()
    for port in Top100Ports:
        if scanner(str(ip),int(port),timeout) == True:
            openCount +=1
        else:
            closedCount +=1

elif choice == 3:
    ip = input("What is the ip you want to scan: ")
    
    start = time.time()
    for port in Top500Ports:
            if scanner(str(ip),int(port),timeout) == True:
                openCount +=1
            else:
                closedCount+=1

elif choice == 4:
    ip = input("What is the ip you want to scan: ")
    portsCount = int(input("How many ports do you want to scan (This will scan the top 'n' Ports you will input): "))
    
    start = time.time()
    for index in range(portsCount):
        if scanner(str(ip), int(list(top_500_ports)[index]), timeout) == True:
            openCount += 1
        else:
            closedCount +=1    
        
        
else:
    print("Incorrect output")
    exit(1)
    
end = time.time()

timer = round(end-start,2)


print(f'\n{Fore.LIGHTYELLOW_EX}Scan Done in {timer} Seconds!')
print(f"{Fore.GREEN}Open Ports: {openCount}")
print(f"{Fore.RED}Closed Ports: {closedCount}")

#print(f"{Fore.BLUE} Amount of Open Ports: {openCount}")
#print(f"{Fore.MAGENTA} Amount of Closed Ports: {closedCount}")

