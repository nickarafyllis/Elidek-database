from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from App import app, db ## initially created by __init__.py, need to be used here
#from App.forms import StudentForm

@app.route("/")
def index():
    try:
        ## create connection to database
        cur = db.connection.cursor()
        ## execute query
        cur.execute("select researcher.first_name, researcher.last_name, count(*) as active_project_number FROM researcher inner join works ON works.researcher_id=researcher.researcher_id inner join project on works.title=project.title where(timestampdiff(year, date_of_birth,current_date())<40 AND current_date()<project.enddate AND current_date()>project.startdate) group by researcher.researcher_id order by count(*) DESC limit 3")
        ## cursor.fetchone() does not return the column names, only the row values
        ## thus we manually create a mapping between the two, the dictionary res
        column_names = [i[0] for i in cur.description]
        res = dict(zip(column_names, cur.fetchone()))
        projectnum1 = res.get("active_project_number")
        best_young_researcher1 = res.get("first_name") + " " + res.get("last_name")
        
        res = dict(zip(column_names, cur.fetchone()))
        projectnum2 = res.get("active_project_number")
        best_young_researcher2 = res.get("first_name") + " " + res.get("last_name")
        
        res = dict(zip(column_names, cur.fetchone()))
        projectnum3 = res.get("active_project_number")
        best_young_researcher3 = res.get("first_name") + " " + res.get("last_name")

        cur.execute("SELECT executive.executive_name, organisation.organisation_name, SUM(amount) as total_sum FROM executive JOIN project ON executive.executive_name=project.executive_name JOIN organisation ON project.organisation_name=organisation.organisation_name join company on organisation.organisation_name=company.organisation_name where own_funds<>0 GROUP BY executive_name ORDER BY SUM(amount) DESC LIMIT 5;")
        column_names = [i[0] for i in cur.description]
        res = dict(zip(column_names, cur.fetchone()))
        cur.close()
        executive_name1 = res.get("executive_name")
        organisation_name1 = res.get("organisation_name")
        total_sum1 = res.get("total_sum")
        
        res = dict(zip(column_names, cur.fetchone()))
        executive_name2 = res.get("executive_name")
        organisation_name2 = res.get("organisation_name")
        total_sum2 = res.get("total_sum")
        
        res = dict(zip(column_names, cur.fetchone()))
        executive_name3 = res.get("executive_name")
        organisation_name3 = res.get("organisation_name")
        total_sum3 = res.get("total_sum")
        
        res = dict(zip(column_names, cur.fetchone()))
        executive_name4 = res.get("executive_name")
        organisation_name4 = res.get("organisation_name")
        total_sum4 = res.get("total_sum")
        
        res = dict(zip(column_names, cur.fetchone()))
        executive_name5 = res.get("executive_name")
        organisation_name5 = res.get("organisation_name")
        total_sum5 = res.get("total_sum") 
        

        return render_template("landing.html",
                               pageTitle = "Home",
                               projectnum1 = projectnum1,
                               projectnum2 = projectnum2,
                               projectnum3 = projectnum3,
                               best_young_researcher1 = best_young_researcher1,
                               best_young_researcher2 = best_young_researcher2,
                               best_young_researcher3 = best_young_researcher3,
                               executive_name1 = executive_name1,
                               executive_name2 = executive_name2,
                               executive_name3 = executive_name3,
                               executive_name4 = executive_name4,
                               executive_name5 = executive_name5,
                               organisation_name1=organisation_name1,
                               organisation_name2=organisation_name2,
                               organisation_name3=organisation_name3,
                               organisation_name4=organisation_name4,
                               organisation_name5=organisation_name5,
                               total_sum1 = total_sum1,
                               total_sum2 = total_sum2,
                               total_sum3 = total_sum3,
                               total_sum4 = total_sum4,
                               total_sum5 = total_sum5
                               )
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
