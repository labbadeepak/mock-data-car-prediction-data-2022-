

import pandas as pd
import numpy as np
import random
import calendar
import os
cars ={
      
      'Maruti Suzuki 800':[28,70],
      'Maruti Suzuki Swift':[24,90],	
      'Honda Amaz':[23,83],	
      'Maruti Suzuki Vitara Brezza':[24,80],
      'Hyundai Creta':[21,75],	
      'nissian kicks':[16,40],	
      'Ford Endeavour':[14,25],	
      'BMW 3 Series':[20,25],	
      'Mercedes benz cls':[16,22],	
      'jagur xf':[13,14],	
      'Nissian GTR':[9,5],	
      'porshe 911':[9,4]	

      }
weights=[cars[car][1] for car in cars]

car_list=[car for car in cars]

columns=['Order ID','Car','Mileage','month','city']

df=pd.DataFrame(columns=columns)
cities=['chennai','mumbai','hyderbad','delhi','bangalore','ahmedabad','puna','kolkata']
city=random.choice(cities)


for month_value in range(1,13):
    
    
    
        if month_value <=9:
           no_of_sales=int(np.random.normal(loc=50,scale=20))

        else:
           no_of_sales=int(np.random.normal(loc=150,scale=20))
    
        month_name=calendar.month_name[month_value] 
    
        orderid=45672

        for i in range(no_of_sales):
            city=random.choice(cities)
            
    
            car=random.choices(car_list,weights=weights)[0]
            orderid+=1
            mileage=cars[car][0]
            df.loc[i]=[orderid ,car,mileage," ",city]
        
        df.to_csv(f"{month_name}_deals_2022.csv")
        
path = "C:\\Users\\labba deepak\\AppData\\Roaming\\Sublime Text\\Packages\\User\\New folder"
files = [file for file in os.listdir(path)] 
mock_data= pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    mock_data = pd.concat([mock_data, current_data])

for monthval in range(1,13):

    monthname=calendar.month_name[monthval] 

mock_data["month"]=random.choice(monthname)

mock_data.to_csv("car_dealer_2022_mock_data.csv", index=False)    

    


