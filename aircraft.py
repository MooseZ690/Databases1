import tkinter as tk #imports tkinter - used for opening windows, buttons etc
import sqlite3 #import the module for conversing with the database
from PIL import Image, ImageTk #these let you control images better, and integrate them into tkinter
import time
from time import sleep #imports the function sleep, allowing to simulate loading

#you need to install pillow through terminal: 'pip install pillow' otherwise the image won't work and probably the rest of the code

buttonwidth = 14 #set width of buttons
windowwidth = 668
windowheight = 650 #lets the window sizing variables be changed later on
aircraftnumber = 1 #initialize the aircraftnumber variable, used to show the ranking of planes for the spec chosen
sql = ''  #initialize the sql variable
results = []  #initialize the results variable as a list
DATABASE = "aircraft.db"
BASE_SELECT = """
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name, country.country_name, engine.engine_name
    FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    INNER JOIN engine ON aircraft.engine = engine.engine_id
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
    for tuple in results: #results is a list of tuples, which are like lists but unchangeable. tuple is each tuple in the list
        placement = '[' + str(aircraftnumber) + ']'
        output_text.insert(tk.END, f"{placement} {tuple[0]}\n", "bold")
        output_text.insert(tk.END, f"Top speed: {"{:,}".format(tuple[1])}km/h\n")
        output_text.insert(tk.END, f"G Limit: {tuple[2]}Gs\n")
        output_text.insert(tk.END, f"Payload: {"{:,}".format(tuple[3])}lbs\n")
        output_text.insert(tk.END, f"Climb Rate: {"{:,}".format(tuple[4])}fpm\n")  
        output_text.insert(tk.END, f"Manufacturer: {tuple[5]}\n")
        output_text.insert(tk.END, f"Country: {tuple[6]}\n")
        output_text.insert(tk.END, f"Engine type: {tuple[7]}\n")
        output_text.insert(tk.END, "━" * 22 + "\n")
        aircraftnumber += 1 #the next aircraft will be one place higher
    output_text.configure(state="disabled") #makes the text box uneditable again
    aircraftnumber = 1 #resets the variable for the next time this function is called

def america():
    global sql
    sql = f'{BASE_SELECT}\n WHERE country.country_id = 1'
    fetch_and_print(sql) 

def russia():
    global sql
    sql = f'{BASE_SELECT}\n WHERE country.country_id = 2'
    fetch_and_print(sql)

def france():
    global sql
    sql = f'{BASE_SELECT}\n WHERE country.country_id = 3'
    fetch_and_print(sql)

def germany():
    global sql
    sql = f'{BASE_SELECT}\n WHERE country.country_id = 4'
    fetch_and_print(sql)

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
root.title("Aircraft Database (11DTP Project)") #names the window
root.geometry(f"{windowwidth}x{windowheight}") #sizes the window, currently just enough to fit the text box sideways


my_font = ("Helvetica", 10, "bold")

speedbutton = tk.Button(root, text="Sort by Speed", font=(my_font), command = print_by_speed, width=buttonwidth) #creates a button in root that runs print_by_speed
speedbutton.grid(row=2, column=0, padx=10, pady=10)
speedbutton.config(bg='black', fg='white')

gbutton = tk.Button(root, text="Sort by G Limit", font=(my_font), command = print_by_g_limit, width=buttonwidth) #creates a button in root that runs print_by_g_limit
gbutton.grid(row=2, column=1, padx=10, pady=10)
gbutton.config(bg='black', fg='white')

payloadbutton = tk.Button(root, text="Sort by Payload", font=(my_font), command = print_by_payload, width=buttonwidth) #creates a button in root that runs print_by_payload
payloadbutton.grid(row=2, column=2, padx=10, pady=10)
payloadbutton.config(bg='black', fg='white')

climbbutton = tk.Button(root, text="Sort by Climb Rate", font=(my_font), command = print_by_climb_rate, width=buttonwidth) #creates a button in root that runs print_by_climb_rate
climbbutton.grid(row=2, column=3, padx=10, pady=10)
climbbutton.config(bg='black', fg='white')

usabutton = tk.Button(root, text='American', font=(my_font), command = america, width=buttonwidth) #creates a button in root that shows all planes from america
usabutton.grid(row=3, column=0, padx=10, pady=10)
usabutton.config(bg='black', fg='white')

rusbutton = tk.Button(root, text='Russian', font=(my_font), command = russia, width=buttonwidth) #creates a button in root that shows all planes from russia
rusbutton.grid(row=3, column=1, padx=10, pady=10)
rusbutton.config(bg='black', fg='white')

frabutton = tk.Button(root, text='French', font=(my_font), command = france, width=buttonwidth) #creates a button in root that shows all planes from france
frabutton.grid(row=3, column=2, padx=10, pady=10)
frabutton.config(bg='black', fg='white')

gerbutton = tk.Button(root, text='German', font=(my_font), command = germany, width=buttonwidth) #creates a button in root that shows all planes from germany
gerbutton.grid(row=3, column=3, padx=10, pady=10)
gerbutton.config(bg='black', fg='white')

output_text = tk.Text(root)
output_text.grid(row=4, column=0, columnspan=4, rowspan=8, padx=10, pady=20) #makes the text box as wide as all the buttons, just below them
output_text.configure(state="disabled", bg='light gray') #makes the text box only output, so the user cant type in it
#i cant use pack because you cant use grid and pack for formatting in the same window - also i don't want to make a new container so i just use the window itself
output_text.tag_configure("bold", font=("TkDefaultFont", 10, "bold")) #makes a bold tag so i can use it in the output text box, tkinter doesn't support rich text formatting


#adding a silhouette of a C5 galaxy just for looks
original_image = Image.open("c5galaxy.png") #imports the image c5galaxy.png from the folder into the code using the Image module from pillow (PIL)
width, height = original_image.size #gets the pixel size of the image 
resized_image = original_image.resize((650, 159)) #uses the resize tool from pillow to change the image to fit the window, i calculated the height by finding the ratio of previous width to the width I want
plane_image = ImageTk.PhotoImage(resized_image) #makes the new image into a tkinter usable thing
image_label = tk.Label(root, image=plane_image, bg='gray') #tkinter turns the image into a label which can be put into the window
image_label.grid(row=1, column=0, columnspan=4, pady=10) #puts the label at the top

bottomtext = tk.Label(root, text="The information presented in this database may not be totally accurate, sources vary.", font=('Arial', 7), bg="gray", fg="light gray")
#bottomtext.grid(row=11, column=0, columnspan=4, pady=10)
#not using this yet as it's not necessary


root.mainloop() #opens the window