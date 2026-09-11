from mysql import connector
from datetime import datetime


class dbconnect():
    def get_connected(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Athul@2003",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None


class EmployeeManager(dbconnect):
    def post(self,**kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connection.cursor()
            query = """
                        insert into employee(name,place,mobile,email,department,salary,joined_date)
                        values(%s,%s,%s,%s,%s,%s,%s)
                    """
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("New Employee Added Successfully....!")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        self.connect = super().get_connected()
        self.cursor = self.connection.cursor()
        query = "select * from employee where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        return record

    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            values=(id,)
            if record!=None:
                query="delete from employee where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Employee Deleted Sucessfully...!")
            else:
                print("Employee Not Found....!")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update employee set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Employee Details Added Successfully...!")
            else:
                print("Member not found...!")
        except Exception as e:
            print(e)






# connection_instance=dbconnect()
# print(connection_instance.get_connected())
#
# employee_instance=EmployeeManager()
# #employee_instance.post(name="Athul",place="Kollam",mobile="8667876353",email="athul@gmail.com",department="python developer",salary=50000,joined_date=datetime.today())
# #employee_instance.post(name="Deepu",place="Pune",mobile="9898676325",email="deepu@gmail.com",department="Senior Chef",salary=100000,joined_date=datetime.today())
# #employee_instance.post(name="Achu",place="Kayamkulam",mobile="9087866353",email="achu@gmail.com",department="software tester",salary=30000,joined_date=datetime.today())
# employee_instance.get()
# employee_instance.retrieve(2)
# #employee_instance.delete(3)
# employee_instance.put(id=2,salary=80000,department="junior chef")
