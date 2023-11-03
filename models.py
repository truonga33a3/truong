from pydoc import describe
from main import db
from sqlalchemy import Sequence, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    user_id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    projects = relationship('Project', back_populates = 'user')

    def __repr__(self):
        return '<User full name: {} {}, email: {}>'.format(self.first_name, self.last_name, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    task_id = db.Column(db.Integer, Sequence('task_id_seq'), primary_key = True)
    description = db.Column(db.String(255), nullable = False)
    deadline = db.Column(db.String(255), nullable = False)

    project_id = db.Column(db.Integer, ForeignKey('project.project_id'))
    project = relationship('Project', back_populates = 'tasks')

    status_id = db.Column(db.Integer, ForeignKey('status.status_id'))
    status = relationship('Status', back_populates = 'tasks')

    priority_id = db.Column(db.Integer, ForeignKey('priority.priority_id'))
    priority = relationship('Priority', back_populates='tasks')

    def __repr__(self):
        return '<Task: {} - {} of project {}'.format(self.task_id, self.description, self.project_id)
    
    def getPriorityClass(self):
        if (self.priority_id == 1):
            return "table-danger"
        elif (self.priority_id == 2):
            return "table-warning"
        elif (self.priority_id == 3):
            return "table-info"
        else:
            return "table-primary"

class Priority(db.Model):
    priority_id = db.Column(db.Integer, Sequence('priority_id_seq'), primary_key = True)
    text = db.Column(db.String(50), nullable = False)
    
    tasks = relationship('Task', back_populates = 'priority')
    
    def __repr__(self):
        return '<Priority: {} with {}>'.format(self.priority_id, self.text)

class Status(db.Model):
    status_id = db.Column(db.Integer, Sequence('status_id_seq'), primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    
    tasks = relationship('Task', back_populates = 'status')
    projects = relationship('Project', back_populates = 'status')
    
    def __repr__(self):
        return '<Status: {} with {}>'.format(self.status_id, self.description)
    
class Project(db.Model):
    project_id = db.Column(db.Integer, Sequence('project_id_seq'), primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    deadline = db.Column(db.Date, nullable = False)
    
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'))
    user = relationship('User', back_populates = 'projects')

    status_id = db.Column(db.Integer, ForeignKey('status.status_id'))
    status = relationship('Status', back_populates = 'projects')
    
    tasks = relationship('Task', back_populates = 'project')
    
    def __repr__(self):
        return '{} {}: {} {}'.format(self.project_id, self.deadline, self.name. self.description)