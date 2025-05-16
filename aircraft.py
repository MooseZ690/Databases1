import tkinter as tk #imports the module for creating windows
import sqlite3
from tkinter import messagebox

sql = ''  #initialize the sql variable
DATABASE = "aircraft.db"

def fetch_and_print(sql):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        results = cursor.execute(sql)
    return results

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


BASE_SELECT = """
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name
    FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
"""

root = tk.Tk()
root.title("Aircraft Database")
root.geometry("800x600")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)


speedbutton = tk.Button(root, text="Sort by Speed", command=print_by_speed)


gbutton = tk.Button(root, text="Sort by G Limit", command=print_by_g_limit)


payloadbutton = tk.Button(root, text="Sort by Payload", command=print_by_payload)


climbbutton = tk.Button(root, text="Sort by Climb Rate", command=print_by_climb_rate)




root.mainloop()