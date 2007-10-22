"""
test the different syntaxes to define fields
"""

from elixir import *

def setup():
    metadata.bind = 'sqlite:///'
        
class TestFields(object):
    def teardown(self):
        cleanup_all(True)
    
    def test_attr_syntax(self):
        class Person(Entity):
            firstname = Field(Unicode(30))
            surname = Field(Unicode(30))

        setup_all(True)
        
        homer = Person(firstname="Homer", surname="Simpson")
        bart = Person(firstname="Bart", surname="Simpson")
        
        session.flush()
        session.clear()
        
        p = Person.get_by(firstname="Homer")
        
        assert p.surname == 'Simpson'

    def test_has_field(self):
        class Person(Entity):
            has_field('firstname', Unicode(30))
            has_field('surname', Unicode(30))

        setup_all(True)
        
        homer = Person(firstname="Homer", surname="Simpson")
        bart = Person(firstname="Bart", surname="Simpson")
        
        session.flush()
        session.clear()
        
        p = Person.get_by(firstname="Homer")
        
        assert p.surname == 'Simpson'
        
    def test_with_fields(self):
        class Person(Entity):
            with_fields(
                firstname = Field(Unicode(30))
                surname = Field(Unicode(30))
            )
            
        setup_all(True)
        
        homer = Person(firstname="Homer", surname="Simpson")
        bart = Person(firstname="Bart", surname="Simpson")
        
        session.flush()
        session.clear()
        
        p = Person.get_by(firstname="Homer")
        
        assert p.surname == 'Simpson'

