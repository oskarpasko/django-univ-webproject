# django-univ-webproject
Web Project for University of Rzeszów for Webb Aplications

## Tytuł projektu
Rejestr napraw telefonów komórkowych

## Pomysły
+ Strona główna
+ Strona z cennikiem napraw
+ Strona z formularzem do rejestracji nowej naprawy
+ Strona z ukończonymi naprawami
+ (Na stronie Admina) strona z naprawami do realizacji

### Baza danych

+ client
  - client_email, PK VC(60) NN UQ
  - client_fname, VC(50) NN
  - client_lname, VC(50) NN
  - client_pass, VC(100) NN
  - client_phone, CHAR(9) 
+ employee
  - employee_email, PK VC(60) NN UQ
  - employee_fname, VC(50) NN
  - employee_lname, VC(50) NN
  - employee_phone, CHAR(9) NN UQ
  - employee_post, FK NN
  - employee_location, FK
+ post
  - post_name, PK VC(50) NN UQ
  - post_salary, FLOAT NN
+ service 
  - service_id, PK INT NN UQ
  - service_name, VC(50) NN
  - serivce_price, FLOAT NN
+ location
  - location_id, PK INT NN UQ
  - location_street, VC(255) NN
  - location_number, VC(5) NN
  - location_postcode, CHAR(6) NN
  - location_phone, CHAR(9)
+ record
  - record_id, PK INT NN UQ
  - record_start_date, DATE NN
  - record_deadline, DATE
  - record_client, FK
  - record_post, FK
  - record_service, FK
  - record_location, FK
