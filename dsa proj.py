import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import csv
from datetime import datetime


def destroy():
    global val
    val = 0
    root.destroy()
    Default()

def Default():
    global x
    global val
    root1 = tk.Tk()
    root1.geometry("800x500")
    root1.title("Parking Manager")
    width= root1.winfo_screenwidth()
    height= root1.winfo_screenheight()
    #set screensize as fullscreen and not resizable
    root1.geometry("%dx%d" % (width, height))
    root1.resizable(True, True)

    imgTemp = Image.open("pm.png")
    img2 = imgTemp.resize((width,height))
    if img2.mode != 'RGBA':
        img2 = img2.convert('RGBA')
    img_op = img2.copy()
    img_op.putalpha(200)
    img = ImageTk.PhotoImage(img_op)
    image_label = tk.Label(root1,image = img)
    image_label.pack(side='top',fill="x",expand=True)
    label = tk.Label(root1, text="Parking Manager", font=("Arial",20))
    label.pack(padx=20, pady=20)
    
    x = int(input("Enter :"))
    occupied.append(x)
    
    if occupied.count(x)<=1:
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%H:%M")
        entry_dict[x] = current_datetime
        root1.destroy()
        allotment()
    elif occupied.count(x)%2==0 and occupied.count(x)>1:
        t = dic[x]
        occupancy[t[0]//2][t[1]//2] = False
        val = 1
        # current_datetime = datetime.now()
        exit_time= datetime.now()
        duration=exit_time-entry_dict[x]
        minutes, seconds = divmod(duration.total_seconds(), 60)
        print(f"{int(minutes)} Minutes {int(seconds)} Seconds")
        root1.destroy()
        allotment()
    root1.mainloop()

def payment():
    url = "https://www.youtube.com/"
    webbrowser.open(url)

def allotment():
    global root
    global occupancy
    global val
    global dic
    global c
    
    root = tk.Tk()
    root.geometry("800x500")
    root.title("New")
    root.attributes('-fullscreen', True)
    root.configure(bg = "white")
    details = cars[x]
    f1 = tk.Frame(root, bg = "white",relief="flat", borderwidth=1)
    f1.pack(side="left", fill="y")
    l = tk.Label(f1,text = "   CAR DETAILS\n\n\nCar Brand : "+details[2]+"\n\nModel : "+details[3]+"\n\nNumber_Plate : "+details[1]+"\n\nFuel type : "+details[4],font=("Arial",20))
    l.pack(padx = 100,pady=130)
    b = tk.Button(text="Collect Receipt",padx=10,pady=10,command=destroy)
    b.pack(pady=50)
    car_img = Image.open("car.jpg")
    car_img = car_img.resize((70,95))
    car_img_g = car_img.copy()
    car_img_g.putalpha(100)
    car_img = ImageTk.PhotoImage(car_img_g)
    car_all = ImageTk.PhotoImage(Image.open("car_all.jpg").resize((70,95)))
    car_occ = ImageTk.PhotoImage(Image.open("car_occ.png").resize((70,95)))
    road_ver = ImageTk.PhotoImage(Image.open("road_ver.png").resize((25,95)))
    road_hor = ImageTk.PhotoImage(Image.open("road_hor.png").resize((76,25)))
    road_mid = ImageTk.PhotoImage(Image.open("road_mid.png").resize((25,25)))
    container = tk.Frame(root)
    container.configure(bg="white")
    container.pack(fill="both", expand=True)
    for row in range(7):
        for column in range(11):
            if row % 2 != 0:
                if column % 2 != 0:
                    frame = tk.Frame(container, width=70, height=90, bg="lightgray", relief="flat")
                    frame.grid(row=row, column=column, padx=0, pady=0)
                    label1 = tk.Label(frame, image=road_mid)
                    label1.pack()
                else:
                    frame = tk.Frame(container, width=70, height=90, bg="lightgray", relief="flat")
                    frame.grid(row=row, column=column, padx=0, pady=0)
                    label1 = tk.Label(frame, image=road_hor)
                    label1.pack()
            elif column % 2 != 0:
                frame = tk.Frame(container, width=70, height=100, bg="lightgray", relief="flat")
                frame.grid(row=row, column=column, padx=0, pady=0)
                label1 = tk.Label(frame, image=road_ver)
                label1.pack()
            elif row%2==0 and column%2==0:              
                if occupancy[row//2][column//2] == True:
                    frame = tk.Frame(container, width=70, height=100, bg="green", relief="solid", borderwidth=1)
                    frame.grid(row=row, column=column, padx=0, pady=0)
                    label1 = tk.Label(frame, image=car_occ)
                    label1.pack()
                elif occupancy[row//2][column//2] == False and val==0:
                    frame = tk.Frame(container, width=70, height=100, bg="lightgray", relief="solid", borderwidth=1)
                    frame.grid(row=row, column=column, padx=0, pady=0)
                    label1 = tk.Label(frame, image=car_all)
                    label1.pack()
                    dic[x] = (row,column)
                    occupancy[row//2][column//2] = True
                    val+=1
                elif occupancy[row//2][column//2] == False and val!=0:
                    frame = tk.Frame(container, width=70, height=100, bg="lightgray", relief="solid", borderwidth=1)
                    frame.grid(row=row, column=column, padx=0, pady=0)
                    label1 = tk.Label(frame, image=car_img)
                    label1.pack()
    print(available)
    print(occupied)
    print(dic)
    root.mainloop()

available = [i for i in range(0,24)]
occupied = []
val=0
occupancy=[[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False]]
entry_dict = {}
dic = {}
c = 0
cars = {}
file = open("car_details.csv","r")
reader = csv.reader(file)
for i in reader:
    cars[int(i[0])] = i[1:]
Default()