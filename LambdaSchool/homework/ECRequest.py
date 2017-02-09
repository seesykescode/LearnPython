import requests

contact_info ={
"email": "hireme@mrjsykes.com",
"lastname": "Sykes",
"name": "Johnathon",
"message": "How am I not myself?"
}

r=requests.post('https://LambdaSchool.com/contact-form', json = contact_info)
