import psycopg2
import database_common


@database_common.connection_handler
def get_mentor_data(cursor):
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name as school_name, schools.country
                      FROM mentors LEFT JOIN schools ON mentors.city=schools.city
                      ORDER BY mentors.id""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_school(cursor):
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name as school_name, schools.country
                      FROM mentors RIGHT JOIN schools ON mentors.city=schools.city
                      ORDER BY mentors.id""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentors_by_country(cursor):
    cursor.execute("""SELECT schools.country, count(schools.country)
                      FROM mentors LEFT JOIN schools ON mentors.city=schools.city
                      GROUP BY country ORDER BY country""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_contacts(cursor):
    cursor.execute("""SELECT schools.name as school_name, mentors.first_name, mentors.last_name
                      FROM schools LEFT JOIN mentors ON schools.contact_person=mentors.id
                      ORDER BY schools.name""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicants(cursor):
    cursor.execute("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                      FROM applicants LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                      WHERE applicants_mentors.creation_date >=  '2016-01-01'
                      ORDER BY applicants_mentors.creation_date DESC""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicants_mentors(cursor):
    cursor.execute("""SELECT applicants.first_name as applicant_f_n, applicants.application_code,
                      mentors.first_name, mentors.last_name
                      FROM applicants LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                      LEFT JOIN mentors ON applicants_mentors.mentor_id=mentors.id
                      ORDER BY applicants.id""")
    names = cursor.fetchall()
    return names
