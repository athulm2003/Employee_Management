import streamlit as st
from employeeviews import EmployeeManager

employee_instance=EmployeeManager()
tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Employee")
    name=st.text_input("Enter Employee Name")
    place=st.text_input("Enter place")
    mobile=st.text_input("Enter Mobile Number")
    email=st.text_input("Enter Email id")
    department=st.text_input("Enter Department")
    salary=st.text_input("Enter Salary")
    joined_date=st.date_input("Enter Joined Date(yyyy/mm/dd)")
    if st.button("Add New Employee"):
        employee_instance.post(name=name,place=place,mobile=mobile,email=email,department=department,salary=salary,joined_date=joined_date)
        st.success("New Employee Added Successfully...!")

with tab2:
    st.title("View Employee Details")
    records=employee_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Records found..!")
