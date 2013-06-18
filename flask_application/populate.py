from flask_application import user_datastore
from flask_application.models import db
def create_roles():
    for role in ('admin', 'developer', 'teacher', 'student'):
        user_datastore.create_role(name=role, description=role)
    db.session.commit()
        
def create_users():
    for u in  (('acbart','Austin Cory Bart', 'acbart@vt.edu','password',['admin'],True),
               ('rcastle','Rick Castle', 'castle@udel.edu','password',['teacher'],True),
               ('lelouch','Lelouch Lamperouge', 'lulu@ashford.com','password',['student'],True),
               ('kirk','James Kirk', 'jtkirk@lp.com','password',['developer'],False)):
        user_datastore.create_user(username=u[0], name=u[1], email=u[2], password=u[3],
                                   roles=u[4], active=u[5])
        db.session.commit()

def populate_data():
	create_roles()
	create_users()