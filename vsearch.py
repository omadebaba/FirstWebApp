import mysql.connector
from flask import request
from DBcm import UseDatabase

def search4vowels(phrase: str) -> set:  
    """Return any vowels found in a supplied phrase. """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:  
    """Return a set of the 'letters found in 'phrase'. """
    return set(letters).intersection(set(phrase)) 

def log_request(req: 'flask_request', res: str) -> None:
        
    """Log details of the Web request and the results """
    
    dbConfig = {
            'host': 'localhost',
            'user': 'omade',
            'password': 'Sunrise2uplagas',
            'database' : 'vsearchlogDB'
    }
    with UseDatabase(dbConfig) as cursor:
    
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values(%s, %s, %s, %s, %s) """
                
    cursor.execute(_SQL, (req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res))