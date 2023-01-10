from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def index():
    return "this is the fastapi"
    
@app.get('about')
def about():
    return "about Us "    


 #this is the backend  start   