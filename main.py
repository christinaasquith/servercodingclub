from flask import Flask, render_template, request, redirect

app = Flask(__name__)

count = 0
comments = []
@app.route('/')
def index():
    global count
    count = count + 1
  #  return 'This website has been visited this many times: ' +str(count)
    return render_template("index.html", count=count, comments=comments)

@app.route("/about")
def about():
    return "this is my about page"
  
@app.route("/add_comment", methods=["POST"])
def add_comment():
    global comments

    comments.append({
      "name": request.form['name'],
      "comment":request.form['comment']
      
    })
    print(request.form["comment"])
    print(request.form["name"])
    return redirect('/', code=302)
  
app.run(host='0.0.0.0', port=81)
