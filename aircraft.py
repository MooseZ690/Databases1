import sqlite3

DATABASE = 'aircraft.db'

def get_countries():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT country_id, country_name FROM country"
        cursor.execute(sql)
        return cursor.fetchall() # Gets all the rows from the query - the country ID and name

def print_aircraft(country_id):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
        SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, 
               aircraft.payload_lbs, aircraft.climb_rate_fpm, 
               manufacturer.manufacturer_name
        FROM aircraft
        INNER JOIN country ON aircraft.country = country.country_id 
        INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
        WHERE country.country_id = ?
        """ # SQL query to join aircraft, country, and manufacturer tables
        cursor.execute(sql, (country_id,))
        aircrafts = cursor.fetchall()
        return aircrafts

def main():
    countries = get_countries() # Runs the get_countries function to show the use the available countries
    print("Available Countries:")
    for country_id, name in countries:
        print(f"{country_id}: {name}")
    country_id = int(input("Select a country by ID to view aircraft:")) #Gets user input for country ID
    return country_id

def get_country_id():
    country_id = main()
    aircraft = print_aircraft(country_id)
for aircraft in aircraft:
    print(f"Aircraft Name: {aircraft[0]}")
    print(f"Top Speed (km/h): {aircraft[1]}")
    print(f"G Limit: {aircraft[2]}")
    print(f"Payload (lbs): {aircraft[3]}")
    print(f"Climb Rate (fpm): {aircraft[4]}")
    print(f"Manufacturer: {aircraft[5]}")
    print("-" * 40)
else:
    print("No relevant aircraft found in the database.")
    print("-" * 40)

if __name__ == "__main__":
    get_country_id()