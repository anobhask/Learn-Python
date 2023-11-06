import threading
import sqlite3
from sqlite3 import Error
emp_data = {
   "emp_id":None
}

emp_id = 1
class employee:
   def __init__(self, emp_id, emp_name, emp_email, emp_band) -> None:
      self.emp_id = emp_id
      self.emp_name = emp_name
      self.emp_email = emp_email
      self.emp_band = emp_band
   def __str__(self) -> str:
      return f"Details about Employee : {self.emp_name}"
   def salary(self) -> int:
      return self.emp_band * 100000
   def print(self) -> None:
      print(f'{self.emp_id}\t{self.emp_name}\t{self.emp_email}\t{self.emp_band}')
def read_data():
   global emp_id
   emp_name = input("Employee Name :")
   emp_mail = input("Employee E-mail :")
   emp_band = input("Employee Band :")
   return {
            "emp_id":emp_id,
            "emp_name":emp_name,
            "emp_mail":emp_mail,
            "emp_band":emp_band
           }
if __name__ == "__main__":
   emp1 = employee(1,"Anoop","Anoop@elephant",4)
   my_emp = read_data()
   print(f"Object details : { str(emp1) }")
   print(f"Employee class { employee }")
   emp2 = employee(my_emp.get('emp_id'),my_emp.get('emp_name'),my_emp.get('emp_mail'),my_emp.get('emp_band'))
   emp2.print()
