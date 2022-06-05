import email
import re 

path = 'Path...'
mail = email.message_from_file(open(path))
mail = mail.as_string()
match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', mail)
print(match)