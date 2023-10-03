import subprocess
import sys
max_hops=1
hop_limit=30
ip_address=sys.argv[1]
destination=""
prev=""
while(True):
    command=f"ping -m {max_hops} {ip_address} -t 1"
    print(f"{max_hops}:",end=" ")
    for i in range(3):
        out=subprocess.run(command, shell=True, capture_output=True)
        output=out.stdout.decode().split("\n")
        try:
            if(output[1].split(" ")[0]=="Request"):
                raise Exception("Request Timed Out")
            destination=output[0].split(" ")[2][1:-2]
            current=output[1].split(" ")[3][:-1]
            temp=prev
            prev=current
            command2=f"ping -t 1 -m {max_hops} {current}"
            out2=subprocess.run(command2,shell=True,capture_output=True)
            output2=out2.stdout.decode().split("\n")
            time= output2[-2].split("/")[4]
            if(current!=temp and temp==""):
                print(f"{current}",end=" ")
            elif(current!=temp):
                print()
                print(f"{current}",end=" ")
            print(f"{time}",end=" ")
        except:
            print("*",end=" ")
    print()
    prev=""
    if(current==destination):
        break
    max_hops+=1
    if(max_hops>hop_limit):
        break
