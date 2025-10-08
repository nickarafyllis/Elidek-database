# ELIDEK Research Grants Database Management System

A full-stack web application for managing research projects, grants, and researcher information for the Hellenic Foundation for Research and Innovation (ELIDEK). Built as part of the undergraduate course "Database Systems" at ECE NTUA.

## Overview

This database management system enables efficient tracking and analysis of research funding in Greece, handling complex relationships between research projects, organizations, researchers, and funding programs. The system supports funding amounts ranging from €100,000 to €1,000,000 and manages multi-year projects with deliverables and evaluation workflows.

### Key Features

- **Project Management**: Track research projects with funding details, timelines, deliverables, and scientific field associations
- **Organization Tracking**: Manage three types of organizations (Universities, Research Centers, and Companies) with distinct budget structures
- **Researcher Database**: Store researcher information, project assignments, and employment history
- **Funding Programs**: Monitor grant programs and their distribution across directorates
- **Advanced Queries**: Execute complex analytical queries including cross-disciplinary research patterns, active project statistics, and funding distribution analysis
- **User-Friendly Interface**: Web-based UI with dropdown menus, filters, and dynamic result updates without SQL knowledge required

## Technology Stack

- **Database**: MySQL (MariaDB)
- **Backend**: Python 3 with Flask framework
- **Frontend**: HTML/CSS
- **Server**: XAMPP Control Panel
- **Version Control**: Git

## Database Schema

The system implements a normalized relational database with the following core entities:

- Research Projects (Grants) with 1-4 year duration constraints
- Organizations (Universities, Research Centers, Companies)
- Researchers and their organizational affiliations
- Funding Programs and Directorates
- Scientific Fields and cross-disciplinary project associations
- Project Deliverables with submission tracking
- Project Evaluations by external reviewers
- ELIDEK Staff managing project administration

## Installation

### Prerequisites

- Python 3.x
- XAMPP Control Panel
- Git

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/nickarafyllis/Elidek-database.git
cd Elidek-database
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start MySQL service from XAMPP Control Panel

4. Initialize the database:
   - Open XAMPP shell
   - Execute SQL scripts in order:
     - `CREATE_tables.sql`
     - `CREATE_views.sql`
     - `CREATE_indexes.sql`

5. Populate database with sample data:
```bash
python insert_data.py
```

6. Launch the application:
```bash
python run.py
```

7. Access the application at `localhost:3000` in your browser

## Dummy Database Features

### Sample Data Volume
- 30+ funding programs
- 50+ research projects (30+ active)
- 30+ organizations across all three categories
- 100+ researchers with complete profiles

### Advanced Query Capabilities

The system supports sophisticated analytical queries including:

- Multi-criteria project filtering (date, duration, staff handler)
- Active projects by scientific field analysis
- Organization funding patterns across consecutive years
- Top-3 interdisciplinary field pair identification
- Young researcher participation statistics (age < 40)
- Top-5 staff members by corporate funding distribution
- Researcher workload analysis for projects without deliverables

### Performance Optimization

Custom indexes designed for query optimization, with detailed justification for each index based on query patterns and performance requirements.

## Database Views

The application includes pre-configured views for:
- Projects per researcher analysis
- Custom analytical view for specialized reporting needs

## Academic Context

**Course**: Database Systems (6th Semester)  
**Institution**: School of Electrical and Computer Engineering, National Technical University of Athens  
**Academic Year**: 2021-2022  
**Team Size**: 3 members (collaborative project)

## Design Constraints

- No ORM frameworks used - all queries implemented in native SQL
- Emphasis on query efficiency and elegance
- Strict referential integrity and domain constraints enforcement
- User-friendly interface requiring no SQL knowledge from end users

## Contributors

- Nikolaos Karafyllis
- Anastasios Safaris
- Ignatios Siminis

## License

MIT License
