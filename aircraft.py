import sqlite3

direction = 'DESC' #defaults to descending order on specifics
countryid = 1 #defaults to first country, in this case america as the majority of aircraft are american
manufacturerid = 1 #defaults to the first manufacturer, in this case boeing

DATABASE = 'aircraft.db'

def print_by_speed():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    ORDER by aircraft.top_speed_kmh {direction}
    """
def print_by_g():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    ORDER by aircraft.top_speed_kmh {direction}
    """
def print_by_payload():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    ORDER by aircraft.top_speed_kmh {direction}
    """
def print_by_climb_rate():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    ORDER by aircraft.top_speed_kmh {direction}
    """
def print_by_manufacturer():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    WHERE manufacturer.manufacturer_id = {manufacturerid}
    """
def print_by_country():
    cursor = f"""
    SELECT aircraft.aircraft_name, aircraft.top_speed_kmh, aircraft.g_limit, aircraft.payload_lbs, aircraft.climb_rate_fpm, manufacturer.manufacturer_name FROM aircraft
    INNER JOIN country ON aircraft.country = country.country_id 
    INNER JOIN manufacturer ON aircraft.manufacturer = manufacturer.manufacturer_id
    WHERE country.country_id = {countryid}
    """
def main():
    print('Super duper cool aircraft database')
    print(
"""Available commands:
Sort by speed - '1'
Sort by g - '2'
Sort by payload - '3'
Sort by climb rate - '4'
Sort by manufacturer - '5'
Sort by country - '6'
"""
    )