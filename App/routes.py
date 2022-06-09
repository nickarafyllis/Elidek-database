from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from App import app, db ## initially created by __init__.py, need to be used here
from App.forms import ResearcherForm, WorksForm

@app.route("/")
def index():
    
    try:
        ## create connection to database
        cur = db.connection.cursor()            
        cur.execute("SELECT program_name from program")
        column_names = [i[0] for i in cur.description]
        programs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

        cur.execute("SELECT * from scientific_field")
        column_names = [i[0] for i in cur.description]
        scifields = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.close()
        return render_template("landing.html",
                               pageTitle = "Home",
                               programs=programs,
                               scifields=scifields                               
                               )
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Home") 

@app.route("/researchers")
def getResearcher():
    """
    Retrieve researchers from database
    """
    try:
        form = ResearcherForm()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM researcher")
        column_names = [i[0] for i in cur.description]
        researcher = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("researchers.html", researcher = researcher, pageTitle = "Researchers Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/researchers/update/<int:researcherID>", methods = ["POST"])
def updateResearcher(researcherID):
    """
    Update a researcher in the database, by id
    """
    form = ResearcherForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE researcher SET first_name = '{}', last_name = '{}', sex = '{}', date_of_birth = '{}', employment_date = '{}', organisation_name = '{}' WHERE researcher_id = {};".format(updateData['first_name'].data, updateData['last_name'].data, updateData['sex'].data, updateData['date_of_birth'].data, updateData['employment_date'].data, updateData['organisation_name'].data, researcherID)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher updated successfully", "success")
        except Exception as e:
            flash(str(e), "error")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getResearcher"))

@app.route("/researchers/delete/<int:researcherID>", methods = ["POST"])
def deleteResearcher(researcherID):
    """
    Delete researcher by id from database
    """
    query = f"DELETE FROM researcher WHERE researcher_id = {researcherID};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getResearcher"))
 
@app.route("/projectperresearcher/")
def getProject():
    """
    Retrieve projects per researcher from database
    """
    try:
        cur = db.connection.cursor()
        cur.execute("SELECT concat(researcher.first_name,' ',researcher.last_name) as full_name, project.title, project.amount, project.startdate, project.enddate from researcher, works, project where researcher.researcher_id=works.researcher_id AND works.title=project.title ORDER BY full_name, project.title;")
        column_names = [i[0] for i in cur.description]
        project = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("view2.html", project = project, pageTitle = "Projects Per Researcher Page")
    except Exception as e:
        abort(500)
        print(e)      

@app.route("/researchers/create", methods = ["GET", "POST"]) ## "GET" by default
def createResearcher():
    """
    Create new researcher in the database
    """
    form1 = ResearcherForm()
    ## when the form is submitted
    if(request.method == "POST" and form1.validate_on_submit()):
        newResearcher = form1.__dict__
        query = "INSERT INTO researcher(first_name, last_name, sex, date_of_birth, employment_date, organisation_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(newResearcher['first_name'].data, newResearcher['last_name'].data, newResearcher['sex'].data, newResearcher['date_of_birth'].data, newResearcher['employment_date'].data, newResearcher['organisation_name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")
            
    form2 = WorksForm()
    ## when the form is submitted
    if(request.method == "POST" and form2.validate_on_submit()):
        newWorks = form2.__dict__
        query = "INSERT INTO works(researcher_id, title) VALUES ('{}', '{}');".format(newWorks['researcher_id'].data, newWorks['title'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Working relationship inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("create_researcher.html", pageTitle = "Create", form1 = form1, form2 = form2)
    
@app.route("/facts")
def facts():
    try:
        ## create connection to database
        cur = db.connection.cursor()
        
        cur.execute("SELECT d.organisation_name, d.projectnum, e.year, d.year from projperyear d inner join projperyear e on d.organisation_name=e.organisation_name where d.year=e.year+1 and d.projectnum=e.projectnum")
        column_names = [i[0] for i in cur.description]
        q4 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.execute("SELECT A.scientific_field_name AS scientificfield1, B.scientific_field_name AS scientificfield2, count(*) as count FROM has A, has B WHERE A.title = B.title and A.scientific_field_name <> B.scientific_field_name and B.scientific_field_name > A.scientific_field_name GROUP by A.scientific_field_name, B.scientific_field_name ORDER BY count desc limit 3")
        column_names = [i[0] for i in cur.description]
        q5 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.execute("SELECT concat(researcher.first_name,' ',researcher.last_name) as full_name, count(*) as active_project_number FROM researcher inner join works ON works.researcher_id=researcher.researcher_id inner join project on works.title=project.title where(timestampdiff(year, date_of_birth,current_date())<40 AND current_date()<project.enddate AND current_date()>project.startdate) group by researcher.researcher_id order by count(*) DESC limit 3")
        column_names = [i[0] for i in cur.description]
        q6 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

        cur.execute("SELECT executive.executive_name, organisation.organisation_name, SUM(amount) as total_sum FROM executive JOIN project ON executive.executive_name=project.executive_name JOIN organisation ON project.organisation_name=organisation.organisation_name join company on organisation.organisation_name=company.organisation_name where own_funds<>0 GROUP BY executive_name ORDER BY SUM(amount) DESC LIMIT 5;")
        column_names = [i[0] for i in cur.description]
        q7 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
       
        cur.execute("select concat(researcher.first_name,' ',researcher.last_name) as full_name , count(*) as project_num from researcher join works on works.researcher_id = researcher.researcher_id where works.title in ( SELECT DISTINCT project.title FROM project WHERE project.title not in (select title from deliverable) ) group by works.researcher_id having count(*)>4 order by project_num desc limit 3;")
        column_names = [i[0] for i in cur.description]
        q8 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.close()
        
        return render_template("facts.html",
                               pageTitle = "Elidek facts",
                               q4=q4,
                               q5=q5,
                               q6=q6,
                               q7=q7,
                               q8=q8
                               )
    except Exception as e:
        print(e)
        return render_template("facts.html", pageTitle = "Elidek facts")
    
@app.route("/program/<string:programname>", methods = ["POST", "GET"])
def getprog(programname):
    """
    Show projects in a program
    """
    query = f"SELECT title, startdate, enddate, executive_name, organisation_name from project join program on project.program_name=program.program_name where program.program_name={programname} order by enddate - startdate desc"
    #query1 = f"SELECT title from project join program on project.program_name=program.program_name where program.program_name={programname} order by enddate - startdate desc" 
    #query2 = f"SELECT title from project join program on project.program_name=program.program_name where program.program_name={programname} order by startdate desc"
    #query3 = f"SELECT title from project join program on project.program_name=program.program_name where program.program_name={programname} order by executive.executive_name"    
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        query = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    
        cur.close()
        return render_template("query1.html", query=query, pageTitle = programname)  #titlos

    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("index"))

@app.route("/researchersinproject/<string:projecttitle>", methods = ["POST", "GET"])
def getres(projecttitle):
    """
    Show researchers in a project
    """
    query = f"SELECT concat(researcher.first_name,' ',researcher.last_name) as full_name from researcher join works on researcher.researcher_id=works.researcher_id join project on works.title=project.title where project.title={projecttitle}"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        query = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    
        cur.close()
        return render_template("researchersinproject.html", query=query, pageTitle = projecttitle) #titlos

    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("index"))
    
@app.route("/projectsfield/<string:scientificfield>", methods = ["POST", "GET"])
def get(scientificfield):
    """
    Show projects and researcher in a specific scientific field
    """
    query1 = f"SELECT project.title FROM project INNER JOIN has on project.title=has.title WHERE(current_date()<project.enddate AND current_date()>project.startdate AND has.scientific_field_name={scientificfield});"
    query2 = f"SELECT concat(researcher.first_name,' ',researcher.last_name) as full_name from researcher inner JOIN works on researcher.researcher_id=works.researcher_id inner join has on works.title= has.title join project on project.title=has.title where(current_date()<enddate AND current_date()>startdate AND timestampdiff(year,startdate, current_date())<1 AND has.scientific_field_name={scientificfield});;"
    try:
        cur = db.connection.cursor()
        cur.execute(query1)
        column_names = [i[0] for i in cur.description]
        project = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.execute(query2)
        column_names = [i[0] for i in cur.description]
        researcher = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        
        cur.close()
        return render_template("projectsfield.html", project = project, researcher=researcher,pageTitle = scientificfield)  #titlos

    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
