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
  - client_fname, VC(25) NN
  - client_lname, VC(25) NN
  - client_pass, VC(100) NN
  - client_phone, CHAR(9) 
+ employee
  - employee_login
  - employee_fname
  - employee_lname
+ record
