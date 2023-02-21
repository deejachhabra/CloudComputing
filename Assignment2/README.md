 provide a local interface (using a web page, displayed in a 
 browser) to a cloud service that you will implement that will allow a user to upload 
 earthquake data and investigate it. (Creating the table doesn’t need to utilize 
 a web interface) 
 There are some “theories”: 
 There are more quakes in the early morning 
 There are more quakes in certain geographic locations (ring of fire) 
 Fewer quakes on weekends 
 And many, many others 
  Please go to: 
 https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
 and get all earth quakes for the last 30 days (bottom right), which is a a .csv file, 
 place these on your cloud service provider and import this into SQL. 
 This page also has a “schema” for the data. 
 Your cloud-based “service” will allow a user to: 
 
  ![image](https://user-images.githubusercontent.com/108027722/220469666-e0e0a527-bd84-4cd0-8b6b-7ebf14493e77.png)
 + Search for and count all earthquakes that occurred with a magnitude greater 
 than 5.0 
 
 ![image](https://user-images.githubusercontent.com/108027722/220469782-2e75584b-f7b1-4083-8002-763bdcd8ebd1.png)
 
 
 + Search for 2.0 to 2.5, 2.5 to 3.0, etc magnitude quakes for a one week, 
 a range of days or the whole 30 days. 

![image](https://user-images.githubusercontent.com/108027722/220469876-26af0b37-4a94-40ad-8004-20095c077f48.png)

![image](https://user-images.githubusercontent.com/108027722/220469933-122c64fd-08c9-4965-b29b-3bbb903b363e.png)

+ Find earthquakes that were near (20 km, 50 km?) of a specified location.

![image](https://user-images.githubusercontent.com/108027722/220471773-428a3dc3-9686-418d-a0da-524b90403e2b.png)

![image](https://user-images.githubusercontent.com/108027722/220471850-1aa1c330-9eeb-4f13-a007-834f184e904d.png)

+ Find clusters of earthquakes 

![image](https://user-images.githubusercontent.com/108027722/220472004-f4fa092b-d320-4f45-b318-dcd3ab11e918.png)

![image](https://user-images.githubusercontent.com/108027722/220472054-01a7fc73-36ae-4de1-8d41-76ec70017e8c.png)

+ Do large (>4.0 mag) occur more often at night? 

![image](https://user-images.githubusercontent.com/108027722/220472157-84458986-32f9-4708-904b-a48087905872.png)

![image](https://user-images.githubusercontent.com/108027722/220472207-26dbfa0a-acf1-43a5-bc63-2b3e35d7442c.png)

+Update magnitude based on location range

![image](https://user-images.githubusercontent.com/108027722/220472291-d4838477-ccb5-4f04-8dfd-7526134c4e04.png)

![image](https://user-images.githubusercontent.com/108027722/220472341-83c8f47e-4e46-4053-b574-45ba9bb2e016.png)




 
 
 
