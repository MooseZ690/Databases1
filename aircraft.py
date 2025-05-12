import sqlite3

DATABASE = 'aircraft.db'

def print_aircraft():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
        SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, 
               aircraft.payload_lbs, aircraft.climb_rate_fpm, 
               manufacturer.manufacturer_name
        FROM aircraft
        INNER JOIN country ON aircraft.country = country.country_id 
        INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
        WHERE country.country_id = 1
        """
        cursor.execute(sql)
        aircrafts = cursor.fetchall()

        if aircrafts:
            for aircraft in aircrafts:
                print(f"Aircraft Name: {aircraft[0]}")
                print(f"Top Speed (km/h): {aircraft[1]}")
                print(f"G Limit: {aircraft[2]}")
                print(f"Payload (lbs): {aircraft[3]}")
                print(f"Climb Rate (fpm): {aircraft[4]}")
                print(f"Manufacturer: {aircraft[5]}")
                print("-" * 40)
                print_aircraft()
        else:
            print("No relevant aircraft found in the database.")
            print("-" * 40)
            print_aircraft()

if __name__ == "__main__":
    print_aircraft()