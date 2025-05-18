import tkinter as tk #imports the module for creating windows
import sqlite3

sql = ''  #initialize the sql variable
DATABASE = "aircraft.db"
results = []  #initialize the results variable
BASE_SELECT = """
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name
    FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
""" #base select statement - joins the foregin keys so i dont have to do it every funcition

def fetch_and_print(sql):
    global results
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results: #results is a list of tuples, which are like lists but unchangeable
        output_text.insert(tk.END, f"Aircraft Name: {row[0]}\n") #inserts the first element of the tuple into the text box

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
root.geometry("668x600") #makes the window 668x600, just enough to fit the text box


speedbutton = tk.Button(root, text="Sort by Speed", command=print_by_speed) #creates a button in root that runs the print_by_speed. 
speedbutton.grid(row=0, column=0, padx=10, pady=10)

gbutton = tk.Button(root, text="Sort by G Limit", command=print_by_g_limit) #creates a button in root that runs the print_by_g_limit.
gbutton.grid(row=0, column=1, padx=10, pady=10)

payloadbutton = tk.Button(root, text="Sort by Payload", command=print_by_payload) #creates a button in root that runs the print_by_payload.
payloadbutton.grid(row=0, column=2, padx=10, pady=10)

climbbutton = tk.Button(root, text="Sort by Climb Rate", command=print_by_climb_rate) #creates a button in root that runs the print_by_climb_rate.
climbbutton.grid(row=0, column=3, padx=10, pady=10)

output_text = tk.Text(root)
output_text.grid(row=1, column=0, columnspan=4, rowspan=10, padx=10, pady=20) #makes the text box as wide as all the buttons, just below them
output_text.configure(state="disabled") #makes the text box only output, so the use cant type in it
#i cant use pack because you cant have grid and pack in the same window
output_text.delete("1.0", tk.END) #idk why but apparently i need to do this to clear preivious responses


root.mainloop()