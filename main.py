from flask import Flask, render_template, request
from Users import Users


a=Users()
a.Default_Users()

app=Flask(__name__)

@app.route('/api/<name>/get/users')
def hell(name):
    return a.RetUsers(n=name)

@app.route('/api/past/users')  # , method = ["POST", 'GET']
#def past():
    #if request.method == 'POST':
        #return a.RetUsers(n=request.form["n"], s=request.form["s"], l=request.form["l"], p=request.form["p"],g=request.form["g"])
    #return render_template('past.html')
def post():
    return render_template('past.html')




@app.route('/api/put/users/<id>')  # , method = ["POST", 'GET']
def put(id):
    return render_template('put.html')
    # if request.method == 'POST':
    # return a.Change_Usersi=id, n=request.form["n"], s=request.form["s"], l=request.form["l"], p=request.form["p"],g=request.form["g"])
    #return a.Change_Users(i=id)

@app.route('/api/delete/users/<id>')
def delete():
    return render_template('past.html')

if __name__ == '__main__':
    app.run()


