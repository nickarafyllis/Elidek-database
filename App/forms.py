from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field
class ResearcherForm(FlaskForm):
    first_name = StringField(label = "First Name", validators = [DataRequired(message = "First name is a required field.")])

    last_name = StringField(label = "Last Name", validators = [DataRequired(message = "Last name is a required field.")])

    sex = StringField(label = "Sex", validators = [DataRequired(message = "Sex is a required field.")])

    date_of_birth = StringField(label = "Date Of Birth", validators = [DataRequired(message = "Date of birth is a required field.")])

    employment_date = StringField(label = "Employment Date", validators = [DataRequired(message = "Employment date is a required field.")])

    organisation_name = StringField(label = "Organisation Name", validators = [DataRequired(message = "Organisation name is a required field.")])

    submit = SubmitField("Create")
    
class WorksForm(FlaskForm):
    researcher_id = StringField(label = "Researcher ID", validators = [DataRequired(message = "Researcher ID is a required field.")])

    title = StringField(label = "Project Title", validators = [DataRequired(message = "Project title is a required field.")])

    submit = SubmitField("Create")
