import sqlite3
import time
from time import sleep


DATABASE = 'cars1.db'

def print_cars():
    engine = input("Enter engine type: ").upper()
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car.car_name, car.top_speed, engine.engine_name from car \n INNER JOIN engine ON car.engine=engine.engine_id \n WHERE engine.engine_name = ? \n ORDER BY car.top_speed DESC"
        cursor.execute(sql, (engine,))
        results = cursor.fetchall()
        if results:
            print(f' \n Cars found with engine {engine}: \n')
            time.sleep(0.3)
            for car in results:
                print(f'[{car[0]}] \n Top Speed: {car[1]} \n Engine: {car[2]} \n')
                time.sleep(0.15)
            print_cars()
        else:
            print(f"No cars found in the database with engine {engine}")
            print_cars()
if __name__ == "__main__":
    print_cars()