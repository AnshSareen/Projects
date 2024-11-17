import random
from datetime import datetime, timedelta
import time
def ParkCar(time_duration,unique_id,slot_num,k):
    while True:
        ask=input("ARE YOU LOOKING FOR A FREE PARKING SLOT?\n     CHOOSE AMONG THE FOLLOWING\n\t    (YES/NO) \nENTER:")
        if(ask.lower()=="yes"):
            time_duration[1][k]=random.randint(1,60)
            k+=1
            for i in range(0,8):
                if(unique_id[1][i]==0):
                    unique_id[1][i]=1
                    slot_num[i]=i
                    print("The time duration entered by you is:",time_duration[1][i])
                    print("You can park your car in slot number: ",unique_id[0][slot_num[i]],"\n")
                    break
                else:
                    continue
            if(i==7):
                print("Now no more space is avialable!")
                break
        else:
            break
    return [time_duration,unique_id,slot_num,k]

def swap(time_duration,slot_num):
    for i in range(7):
        for j in range(i+1,8):
            if(time_duration[1][i]>time_duration[1][j]):
                temp1=time_duration[1][i]
                time_duration[1][i]=time_duration[1][j]
                time_duration[1][j]=temp1

                temp2=time_duration[0][i]
                time_duration[0][i]=time_duration[0][j]
                time_duration[0][j]=temp2

                temp3=slot_num[i]
                slot_num[i]=slot_num[j]
                slot_num[j]=temp3
    return [time_duration,slot_num]

def intro():

    print("\n\n\n\n\n\n\t\t\t\t---PARKING MANAGEMENT SYSTEM---     ")
    now=datetime.now()
    print(f"\t\t\t\t\t  CURRENT TIME\n\t\t\t\t\t      {now.strftime('%H:%M')}")
    return now


#INTRO
now=intro()


#INITIALIZATION
time_passed=0
fine=10
k=0
time_duration=[[101,102,103,104,105,106,107,108],[100]*8]
unique_id=[[101,102,103,104,105,106,107,108],[0]*8]
slot_num=[0]*8



#PARKING CAR FUNCTION
list1=list(ParkCar(time_duration,unique_id,slot_num,k))
time_duration=list1[0]
unique_id=list1[1]
slot_num=list1[2]
k=list1[3]


#SWAP FUNCTION
list2=list(swap(time_duration,slot_num))
time_duration=list2[0]
slot_num=list2[1]


for x in range(0,k):
    
    if(time_duration[1][x]<30):
        if(x==0):
            for j in range (0,time_duration[1][x]):
                time.sleep(0.25)
                minutes_to_add = j+1
                time_delta = timedelta(minutes=minutes_to_add)
                new_time = now + time_delta
                new_time_formatted = new_time.strftime("%H:%M")
                print({new_time_formatted})
                j+=1
            now=new_time
            print(f"Time when slot:",unique_id[0][slot_num[x]],"becomes vacant:",{new_time_formatted})
            time_passed=time_duration[1][x]
            unique_id[1][slot_num[x]]=0 
            print("Slot number",unique_id[0][slot_num[x]],"is now vacant.\n")
            continue
        if(x>=1):
            for j in range(0,time_duration[1][x]-time_duration[1][x-1]):
                time.sleep(0.25)
                minutes_to_add = j+1
                time_delta = timedelta(minutes=minutes_to_add)
                new_time = now + time_delta
                new_time_formatted = new_time.strftime("%H:%M")
                print({new_time_formatted})
                continue
        now=new_time
        print(f"Time when slot:",unique_id[0][slot_num[x]],"becomes vacant:",{new_time_formatted})
        time_passed=time_duration[1][x]
        unique_id[1][slot_num[x]]=0 
        print("Slot number",unique_id[0][slot_num[x]],"is now vacant.\n")
    else:
        for j in range(0,time_duration[1][x]-time_passed):
            time.sleep(0.5)
            minutes_to_add = j+1
            time_delta = timedelta(minutes=minutes_to_add)
            new_time = now + time_delta
            new_time_formatted = new_time.strftime("%H:%M")
            print({new_time_formatted})
            if(j>=31):
                continue
            if(j==30-time_passed-1):
                for z in range(0,k):
                    if(unique_id[1][slot_num[x]]==1):
                            unique_id[1][slot_num[x]]==0
                            print("Slot number",unique_id[0][slot_num[x]],"is now vacant.")
                            print(f"Time when slot:",unique_id[0][slot_num[x]],"becomes vacant:",{new_time_formatted})
                            print("Person who parked in slot number",unique_id[0][slot_num[x]],":" )
                            print("You exceeded your parking time limit!")
                            break
        time_passed=time_duration[1][x]
        now=new_time
        fine=(time_duration[1][x]-30)*10
        print("Kindly pay the specified fine:",fine,"\n")


    

    


