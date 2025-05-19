import tkinter as tk #imports the module for creating windows
import sqlite3
from PIL import Image, ImageTk

#you need to install pillow through terminal: 'pip install pillow' otherwise the image won't work

aircraftnumber = 1 #initialize the aircraftnumber variable, used to show the ranking of planes
sql = ''  #initialize the sql variable
results = []  #initialize the results variable
DATABASE = "aircraft.db"
BASE_SELECT = """
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name, country.country_name
    FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
""" #base select statement - joins the foregin keys so i dont have to do it every funcition
#this isnt ai sir, i used a triple quote so i didnt have to use \n for each new line


def fetch_and_print(sql):
    global results, aircraftnumber #makes these variables global so they can be used in the function
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    output_text.configure(state="normal") #makes the text box editable just while inserting resylts
    output_text.delete(1.0, tk.END)
    for skibidi in results: #results is a list of tuples, which are like lists but unchangeable
        
        output_text.insert(tk.END, f"[{aircraftnumber}] {skibidi[0]}\n")
        output_text.insert(tk.END, f"Top speed: {skibidi[1]}km/h\n")
        output_text.insert(tk.END, f"G Limit: {skibidi[2]}\n")
        output_text.insert(tk.END, f"Payload: {skibidi[3]}lbs\n")
        output_text.insert(tk.END, f"Climb Rate: {skibidi[4]}fpm\n")
        output_text.insert(tk.END, f"Manufacturer: {skibidi[5]}\n")
        output_text.insert(tk.END, f"Country: {skibidi[6]}\n")
        output_text.insert(tk.END, "------------------------\n")
        aircraftnumber += 1 #the next aircraft will be one higher
    output_text.configure(state="disabled") #makes the text box uneditable again
    aircraftnumber = 1 #resets the variable for the next time this function is called

def print_by_speed():
    global sql
    sql = f'{BASE_SELECT}\n ORDER BY aircraft.top_speed_kmh DESC'
    fetch_and_print(sql)

def print_by_g_limit():
    global sql
    sql = f'{BASE_SELECT}\n ORDER BY aircraft.g_limit DESC'
    fetch_and_print(sql)

def print_by_payload():
    global sql
    sql = f'{BASE_SELECT}\n ORDER BY aircraft.payload_lbs DESC'
    fetch_and_print(sql)
    
def print_by_climb_rate():
    global sql
    sql = f'{BASE_SELECT}\n ORDER BY aircraft.climb_rate_fpm DESC'
    fetch_and_print(sql)


root = tk.Tk() #creates a window called root
root.configure(bg="gray") #sets the background color of the window
root.title("Aircraft Database") #names the window
root.geometry("668x610") #makes the window 668x600, just enough to fit the text box


speedbutton = tk.Button(root, text="Sort by Speed", command = print_by_speed) #creates a button in root that runs the print_by_speed. 
speedbutton.grid(row=2, column=0, padx=10, pady=10)

gbutton = tk.Button(root, text="Sort by G Limit", command = print_by_g_limit) #creates a button in root that runs the print_by_g_limit.
gbutton.grid(row=2, column=1, padx=10, pady=10)

payloadbutton = tk.Button(root, text="Sort by Payload", command = print_by_payload) #creates a button in root that runs the print_by_payload.
payloadbutton.grid(row=2, column=2, padx=10, pady=10)

climbbutton = tk.Button(root, text="Sort by Climb Rate", command = print_by_climb_rate) #creates a button in root that runs the print_by_climb_rate.
climbbutton.grid(row=2, column=3, padx=10, pady=10)

output_text = tk.Text(root)
output_text.grid(row=3, column=0, columnspan=4, rowspan=10, padx=10, pady=20) #makes the text box as wide as all the buttons, just below them
output_text.configure(state="disabled") #makes the text box only output, so the user cant type in it
#i cant use pack because you cant use grid and pack for formatting in the same window


#adding a sillhouette of a C5 galaxy just for looks hehe
original_image = Image.open("c5galaxy.png")
width, height = original_image.size #gets the pixel size of the image
new_width = 650 #because the window is 668x600 having width at 650 prevents clipping
new_height = int(height * (new_width / width)) #to retain the aspect ratio, calculates the width because the ratio from old to new is new/old
resized_image = original_image.resize((new_width, new_height)) #uses the resize tool from pillow to change the image to fit the window
plane_image = ImageTk.PhotoImage(resized_image) #makes the new image into a tkinter usable thing
image_label = tk.Label(root, image=plane_image, bg='gray') #tkinter turns the image into a label
image_label.grid(row=1, column=0, columnspan=4, pady=10) #puts the label at the top

root.mainloop() #opens the window