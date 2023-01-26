# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:13:59 2022

@author: Arne Jandt + Ammar Khidir
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
car_prices = []
car_versions = []
car_details = []
car_kilometerstand = []
car_erstzulassung = []
car_leistung = []
car_gebraucht_oder_new = []
car_fahrzeughalter = []
car_getriebe = []
car_kraftstoff = []
car_verbrauch = []
car_co2_ausstoss = []
lists_of_websites = [ 'https://www.autoscout24.de/lst/bmw/z1?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=y47p4y0b76',
                     'https://www.autoscout24.de/lst/bmw/z3?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=25m2fnith57',
                     'https://www.autoscout24.de/lst/bmw/z4?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=9zwhjn5ocq',
                     'https://www.autoscout24.de/lst/bmw/z8?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=6ybxvunik2',
                     'https://www.autoscout24.de/lst/bmw/x7?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=2cs339reomj',
                     'https://www.autoscout24.de/lst/bmw/x5?sort=standard&desc=0&cy=D&atype=C&ustate=N%2CU&powertype=kw&ocs_listing=include&search_id=xi2ibi4cxm',
                     ]


# Websites durchgehen
for site in lists_of_websites:
    for i in range(2,20,1):
        website = site + str(i)
        #HTTP Agent
        response = requests.get(website)
        
        print(response.status_code)
        
        #Soup Objekt
        soup = BeautifulSoup(response.content,'html.parser')
        
        soup.prettify()
        
        vehicle_details = soup.find_all('div',{'class':'VehicleDetailTable_container__mUUbY'})
        vehicle_details_items = soup.find_all('span',{'class':'VehicleDetailTable_item__koEV4'})
        x3_versions = soup.find_all('span',{'class':'ListItem_version__jNjur'})    
        price_details = soup.find_all('p',{'class':'Price_price__WZayw'})
        
        if len(vehicle_details) != 20:
            continue
        if len(x3_versions) != 20:
            continue
        if len(price_details) != 20:
            continue
        
        # Listen für gescrapte Daten
        print(i)
        #Befuellung der Listen mit for-Schleifen
        for price in price_details:
            try:
                car_prices.append(price.text.strip())
            except:
                car_prices.append('n/a')
        
        for car in x3_versions:
            try:
                car_versions.append(car.text.strip())
            except:
                car_versions.append('n/a')
        
        for vehicle in vehicle_details:
            try:
                car_details.append(vehicle.text.strip())
            except:
                car_details.append('n/a')
        count =1
        for vehicle in vehicle_details_items:
            try:
               if count ==1:
                   car_kilometerstand.append(vehicle.text.strip())
                   count += 1
               elif count ==2:
                   car_erstzulassung.append(vehicle.text.strip())
                   count += 1
               elif count ==3:
                   car_leistung.append(vehicle.text.strip())
                   count += 1    
               elif count ==4:
                   car_gebraucht_oder_new.append(vehicle.text.strip())
                   count += 1
               elif count ==5:
                   car_fahrzeughalter.append(vehicle.text.strip())
                   count += 1
               elif count ==6:
                   car_getriebe.append(vehicle.text.strip())
                   count += 1
               elif count ==7:
                   car_kraftstoff.append(vehicle.text.strip())
                   count += 1
               elif count ==8:
                   car_verbrauch.append(vehicle.text.strip())
                   count += 1    
               elif count ==9:
                   car_co2_ausstoss.append(vehicle.text.strip())
                   count = 1 
                   
            except:
                car_details.append('n/a')

# Laenge der Listen
print(len(car_details))
print(len(car_versions))
print(len(car_prices))
rows = len(car_prices)
# Listen werden in DataFrame zusammengefügt
car_data_bmw = pd.DataFrame({'Version':car_versions[0:rows],'Price':car_prices[0:rows]
                         ,'car_kilometerstand': car_kilometerstand[0:rows]
                         ,'car_erstzulassung': car_erstzulassung[0:rows]
                         ,'car_leistung': car_leistung[0:rows]
                         ,'car_gebraucht_oder_new': car_gebraucht_oder_new[0:rows]
                         ,'car_fahrzeughalter': car_fahrzeughalter[0:rows]
                         ,'car_getriebe': car_getriebe[0:rows]
                         ,'car_kraftstoff': car_kraftstoff[0:rows]
                         ,'car_verbrauch': car_verbrauch[0:rows]
                         ,'car_co2_ausstoss': car_co2_ausstoss[0:rows]})

#Daten in Excel-Datei schreiben
car_data_bmw.to_excel('',index=False)
