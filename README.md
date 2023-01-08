# Gym-Database-Project
## Required tools
In order to execute the script Python is needed to be installed on the machine.
Python 3.11.1 was used and can be downloaded from [here](https://www.python.org/downloads/)

## Contents
- [Gym Database creation python file](https://github.com/G0gg0S/Gym-Database-Project/blob/master/create_database.py)
- [Database fake data insertion python file](https://github.com/G0gg0S/Gym-Database-Project/blob/master/insert_dummy_data.py)
- [User interface application python file](https://github.com/G0gg0S/Gym-Database-Project/blob/master/db_interface.py)

## Execution instructions
- Clone this repository on your desired location.
- Open Command Prompt and navigate the downloaded repository folder.
- Execute the command ***python create_database.py*** to create the database file
- Execute the command ***python insert_dummy_data.py*** to insert the fake pregenerated data to the database
  which are loaded from the csv files located in the [data](https://github.com/G0gg0S/Gym-Database-Project/tree/master/data) folder
- Execute the command ***python db_interface.py*** to open the user interface application and interact with the Gym database

## Insertion procedure example
- Once you run the interface script it will request you for the desired action. We typed ***I*** for insertion.

![Screenshot_1](https://user-images.githubusercontent.com/40723677/211214832-f8931a33-c52f-4e0f-a0b5-54ad6fda9cf8.png)

- Then you should enter the category you would like to have an insertion at. We typed ***3*** for ***Member*** insertion

![Screenshot_2](https://user-images.githubusercontent.com/40723677/211214839-3fdd64ed-a88f-4020-b539-a2ecca089c11.png)

- Finally you should provided the requested data to complete the insertion.

![Screenshot_3](https://user-images.githubusercontent.com/40723677/211214842-08c3d295-313a-4e1e-81d2-68b7dbd0ecc3.png)

## Delete procedure example
- Once you run the interface script it will request you for the desired action. We typed ***D*** for insertion.

![Screenshot_4](https://user-images.githubusercontent.com/40723677/211215188-0a0a2734-d220-4405-b961-265244a2a03f.png)

- Then you should enter the category you would like to have an deletion at. We typed ***6*** for ***Equipment*** deletion

![Screenshot_1](https://user-images.githubusercontent.com/40723677/211215171-d434ad3a-39e1-4baf-99ca-dace6d845b5a.png)

- Finally you should provided the requested ID to complete the deletion. We typed ***1*** to delete the ***Equipment*** with ***ID = 1***
 
![Screenshot_2](https://user-images.githubusercontent.com/40723677/211215178-2f5ad9f5-8f9d-4882-a4b1-c27abe73cf1a.png)

## Update procedure example 
- Once you run the interface script it will request you for the desired action. We typed ***U*** for insertion.

![Screenshot_3](https://user-images.githubusercontent.com/40723677/211215605-03d161c1-bbf6-47d6-98a5-92f3c2d4748e.png)

- Then you should enter the category you would like to have an update at. We typed ***6*** for ***Gym*** update

![Screenshot_1](https://user-images.githubusercontent.com/40723677/211215657-c16e28bb-bec1-4a36-8f99-9c23177d5592.png)

- You should provide the requested ID to update. We typed ***1*** to update.

![Screenshot_2](https://user-images.githubusercontent.com/40723677/211215707-f1f9d74a-692c-4bc6-916e-892b0a8c0047.png)

- The you should provide which attributes to update. We picked ***2,3*** for ***Town and Capacity***

![Screenshot_4](https://user-images.githubusercontent.com/40723677/211215794-04ac426c-00f1-4204-86fd-d7384a693e87.png)

- Finally you should insert the updated values. We typed ***Patras*** and ***300*** for ***Town*** and ***Capacity*** respectively.

![Screenshot_5](https://user-images.githubusercontent.com/40723677/211215854-7105ee65-c9b8-4db7-8776-7efa554995c3.png)

