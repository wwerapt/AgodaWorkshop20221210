# AgodaWorkshop20221210
This is template for students to contribute and use

###Property Hunting
Write a console application having below features
- ```User Registration``` _A user should be able to provide user details and register_
  - ```Input``` _User details (Try to think what is needed)_
  - ```Output``` _Saved user details_
- ```Add Property``` _A registered user should be able to add a property that he want to rent/sell_
  - ```Input``` _Property details_
  - ```Output``` _Saved property_
- ```Search Property``` _Properties can be searched based on parameters_
  - ```Input``` 
    - _Property name_
    - _Property type (1 bhk/2 bhk etc.)_
    - _Property size range (20 to 30 sqm or 30 to 50 sqm etc.)_
    - _Think about more parameters_
  - ```Output``` _Property list meeting the criteria with the user details_
- ```**(BONUS)** Make Appointment``` _Make appointment with the person who listed_
  - ```Input``` _PropertyId, requester details, suitable time etc._
  - ```Output``` _Appointment details like Listing owner, appointment time, requester details etc._

### Mysql Container
```angular2html
Steps to run container
1. Open terminal
2. Go under docker folder and execute command 
    docker-compose up
3. To check status of mysql server, execute 
    docker-compose ps
4. To stop container, execute
    docker-compose down
5. To connect to mysql via. command line
    docker exec -it mysql /bin/bash
    mysql -uroot -pmysql_pass
6. To test a query 
    select * from agoda_workshop.workshop_table;
```