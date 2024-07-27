import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
   print('Request for index page received')
   return render_template('index.html')
   

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/select_user', methods=['POST'])
def transit_to_select_user_page():
   name = request.form.get('task')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('select_user.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
   
@app.route('/registered', method=['post'])
def registered():
    worker = request.form.get('worker')
    name = request.form.get('task')
    
    if worker:
       print('Request for hello page received with name=%s' % worker)
       return render_template('register.html', worker = worker, name = task)
    else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))




if __name__ == '__main__':
   app.run(debug=True)
