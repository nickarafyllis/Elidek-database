import mysql.connector
import pandas as pd
#import numpy as np

Programs = pd.read_csv("./Data/programs.csv")
scientific_fields= pd.read_csv("./Data/scientific_field.csv")
executives = pd.read_csv("./Data/executive.csv")
assessments = pd.read_csv("./Data/assessment.csv")
location_address = pd.read_csv("./Data/location_address.csv")
organisations = pd.read_csv("./Data/organisation.csv")
organisation_types = pd.read_csv("./Data/organisation_type.csv")
phone_numbers = pd.read_csv("./Data/phone_numbers.csv")
researchers = pd.read_csv("./Data/researcher.csv")
projects = pd.read_csv("./Data/projects.csv")
has = pd.read_csv("./Data/has.csv")
deliverables = pd.read_csv("./Data/deliverable.csv")
works = pd.read_csv("./Data/works.csv")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "HFRIManagement"
)

mycursor = mydb.cursor()

for i in range(len(Programs)):
#   program_name,directorate
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() #Save Data
#       sqlFormula = """INSERT INTO customer_phone (card_id,phone_number)
 #                       VALUES ({},{})""".format(i+1,np.random.choice())
  #      mycursor.execute(sqlFormula)
   # mydb.commit() #Save Data
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
    
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()  
   
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(Programs)):  
    program_name = Programs['program_name'][i].replace("'","").replace('"',"")
    directorate= Programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
 
 
 
 
 
 
 
 
 
 
   
mydb.close()
 
print("All Done! Bye, for now.")

