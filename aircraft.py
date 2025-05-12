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
        """
        cursor.execute(sql)
        aircrafts = cursor.fetchall()

        for aircraft in aircrafts:
            print(aircraft)

if __name__ == "__main__":
    print_aircraft()