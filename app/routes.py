from flask import (
    Flask,
    render_template,
    request
)


app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1/:5000/tasks"


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/tasks")  # Corrected route decorator
def task_list():
    response = request.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
    return render_template("list.html", tasks=task_list)


@app.get("/tasks/<int:pk>")
def detail(pk):  # Remove trailing whitespace
    # sourcery skip: replace-interpolation-with-fstring
    url = "%s/%s" % (BACKEND_URL, pk)
    response = request.get(url)
    if response.status_code == 200:
        task = response.json().get("task")
        return render_template("detail.html", task=task)
    return (
        render_template("error.html", err=response.status_code),
        response.status_code
    )
