CREATE VIEW projects_per_researcher
AS
select concat(researcher.first_name,' ',researcher.last_name) as full_name, project.title
from researcher, works, project
where researcher.researcher_id=works.researcher_id
AND works.project_id=project.program_id
order by full_name,project.title;


CREATE VIEW projects_per_scientific_field
AS
select scientific_field.scientific_field_name, project.title
from scientific_field, project, has
where scientific_field.scientific_field_id = has.scientific_field_id
AND has.project_id = project.project_id
order by scientific_field.scientific_field_name, project.title;