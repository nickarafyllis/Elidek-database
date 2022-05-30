import mysql.connector
import pandas as pd
import numpy as np
#from dateutil import relativedelta

programs = pd.read_csv("./Data/programs.csv")
scientific_fields= pd.read_csv("./Data/scientific_fields.csv")
executives = pd.read_csv("./Data/executives.csv")
assessments = pd.read_csv("./Data/assessments.csv")
location_address = pd.read_csv("./Data/address.csv")
organisations = pd.read_csv("./Data/organisations.csv")
organisation_types = pd.read_csv("./Data/organisation_type.csv")
phone_numbers = pd.read_csv("./Data/phone_numbers.csv")
researchers = pd.read_csv("./Data/researchers.csv")
projects = pd.read_csv("./Data/projects.csv")
has = pd.read_csv("./Data/has.csv")
deliverables = pd.read_csv("./Data/deliverable.csv")
works = pd.read_csv("./Data/works.csv")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = '',
    database = "HFRIManagement"
)

mycursor = mydb.cursor()

for i in range(len(programs)):
#   program_name,directorate
    program_name = programs['program_name'][i].replace("'","").replace('"',"")
    directorate= programs['directorate'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO program (program_name,directorate) 
                    VALUES ('{}','{}')""".format(program_name,directorate)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() #Save Data

for i in range(len(scientific_fields)):  
    #scientific_field_name
    scientific_field_name = scientific_fields['scientific_field_name'][i].replace("'","").replace('"',"")

    sqlFormula = """INSERT INTO scientific_field (scientific_field_name) 
                    VALUES ('{}')""".format(scientific_field_name)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
    
for i in range(len(executives)):  
    executive_name = executives['executive_name'][i].replace("'","").replace('"',"")

    sqlFormula = """INSERT INTO executive (executive_name) 
                    VALUES ('{}')""".format(executive_name)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()
 
for i in range(len(assessments)):  
    grade = assessments['grade'][i]
    assessment_date = assessments['assessment_date'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO assessment (grade,assessment_date) 
                    VALUES ('{}','{}')""".format(grade,assessment_date)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()  

 
for i in range(len(location_address)):  
    postal_code = location_address['postal_code'][i]
    street= location_address['street'][i].replace("'","").replace('"',"") 
    city= location_address['city'][i].replace("'","").replace('"',"") 

    sqlFormula = """INSERT INTO location_address (postal_code,street,city) 
                    VALUES ('{}','{}','{}')""".format(postal_code,street,city)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(organisations)):  
    organisation_name = organisations['organisation_name'][i].replace("'","").replace('"',"")
    abbreviation = organisations['abbreviation'][i].replace("'","").replace('"',"")
    location_address_id = organisations['location_address_id'][i]

    sqlFormula = """INSERT INTO organisation (organisation_name,abbreviation,location_address_id) 
                    VALUES ('{}','{}','{}')""".format(organisation_name,abbreviation,location_address_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(organisation_types)):  
    own_funds = organisation_types['own_funds'][i]
    budget_ministry= organisation_types['budget_ministry'][i]
    budget_private_actions= organisation_types['budget_private_actions'][i]
    budget_ministry2= organisation_types['budget_ministry2'][i]

    sqlFormula1 = """INSERT INTO company (own_funds) 
                    VALUES ('{}')""".format(own_funds)
    sqlFormula2 = """INSERT INTO university (budget_ministry) 
                    VALUES ('{}')""".format(budget_ministry)
    sqlFormula3 = """INSERT INTO research_center (budget_private_actions,budget_ministry) 
                    VALUES ('{}','{}')""".format(budget_private_actions,budget_ministry2)
                    
    mycursor.execute(sqlFormula1)
    mycursor.execute(sqlFormula2)
    mycursor.execute(sqlFormula3)
    mydb.commit()
 
for i in range(len(phone_numbers)):  
    phone_number = phone_numbers['phone_number'][i].replace("'","").replace('"',"")
    organisation_id = phone_numbers['organisation_id'][i]

    sqlFormula = """INSERT INTO phone (phone_number,organisation_id) 
                    VALUES ('{}','{}')""".format(phone_number,organisation_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(researchers)):  
    first_name = researchers['first_name'][i].replace("'","").replace('"',"")
    last_name = researchers['last_name'][i].replace("'","").replace('"',"")
    sex = researchers['sex'][i].replace("'","").replace('"',"")
    date_of_birth = researchers['date_of_birth'][i]
    employment_date = researchers['employment_date'][i]
    organisation_id = researchers['organisation_id'][i]

    sqlFormula = """INSERT INTO researcher (first_name,last_name,sex,date_of_birth,employment_date,organisation_id) 
                    VALUES ('{}','{}','{}','{}','{}','{}')""".format(first_name,last_name,sex,date_of_birth,employment_date,organisation_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(projects)):  
    title = projects['title'][i].replace("'","").replace('"',"")
    summary = projects['summary'][i].replace("'","").replace('"',"") 
    amount = projects['amount'][i]
    startdate = projects['startdate'][i].replace("'","").replace('"',"") 
    enddate = projects['enddate'][i].replace("'","").replace('"',"") 
    #duration = relativedelta.relativedelta(enddate, startdate).years
    program_id = projects['program_id'][i]
    organisation_id = projects['organisation_id'][i] 
    executive_id = projects['executive_id'][i]
    supervisor_id = projects['supervisor_id'][i]
    assessor_id = projects['assessor_id'][i]
    assessment_id = projects['assessment_id'][i]

    sqlFormula = """INSERT INTO project (title,summary,amount,startdate,enddate,program_id,organisation_id,executive_id,supervisor_id,assessor_id,assessment_id) 
                    VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(title,summary,amount,startdate,enddate,program_id,organisation_id,executive_id,supervisor_id,assessor_id,assessment_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 

for i in range(len(has)):  
    scientific_field_id = has['scientific_field_id'][i]
    project_id = has['project_id'][i]

    sqlFormula = """INSERT INTO has (project_id,scientific_field_id) 
                    VALUES ('{}','{}')""".format(project_id,scientific_field_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(deliverables)):  
    deliverable_title = deliverables['deliverable_title'][i].replace("'","").replace('"',"")
    summary= deliverables['summary'][i].replace("'","").replace('"',"") 
    delivery_date = deliverables['delivery_date'][i].replace("'","").replace('"',"")
    project_id = deliverables['project_id'][i]

    sqlFormula = """INSERT INTO deliverable (title,summary,delivery_date,project_id) 
                    VALUES ('{}','{}','{}','{}')""".format(deliverable_title,summary,delivery_date,project_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit() 
 
for i in range(len(works)):  
    researcher_id = works['researcher_id'][i]
    project_id = works['project_id'][i]

    sqlFormula = """INSERT INTO works (researcher_id,project_id) 
                    VALUES ('{}','{}')""".format(researcher_id,project_id)
                    
    mycursor.execute(sqlFormula)
    mydb.commit()  
 
 
mydb.close()
 
print("All Done! Bye, for now.")