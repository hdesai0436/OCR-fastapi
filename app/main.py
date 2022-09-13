from re import template
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib

BASE_DIR =pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR/ "templates"))

app = FastAPI()


@app.get('/', response_class=HTMLResponse) #get return json
def home_view(reqest:Request):
    return templates.TemplateResponse('home.html',{'request':reqest})

@app.post('/') #post
def home_detai_view():
    return {"hello":'world'}