import re, sns_sqlite 
from sns_sqlite import exec, select 

def post_a_senryu(user_id, senryu):
    senryu_id = exec('''
        INSERT INTO posted_senryu (user_id, contents)
        VALUES (?,?)''',
    user_id, senryu)
    return senryu_id

def get_all_senryu():
    a = select('SELECT * FROM posted_senryu ORDER BY id DESC LIMIT 50')
    return a

def get_user_senryu(user_id):
    a = select('SELECT * FROM posted_senryu WHERE user_id=(?) ORDER BY id DESC LIMIT 50', user_id)
    return a
def delete_senryu(id, user_id):
    return_value = exec('DELETE FROM posted_senryu WHERE id = (?) AND user_id = (?)',id,user_id)
    return return_value