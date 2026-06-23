from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def exercicio():
    return """
<html>
 <head>
      </head>
      <body>
      <h1>Olá mundo</h1>
      </body>
</html>
"""
