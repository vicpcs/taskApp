from flask import Flask, request, jsonify
app = Flask(__name__)

tasks = []

def post_task():
    task_json = request.get_json(force=True)
    task_val = task_json.get('task')
    tasks.append(task_json)
    return(f'The task you added is: {task_val}')

def get_tasks():
  response = {}
  response.update({'tasks': tasks})
  return(jsonify(response))

@app.route('/health')
def health_check():
  return('Application Status: Running')

@app.route('/task', methods=['GET', 'POST'])
def handle_task_request():
  if(request.method == 'POST'):
    return post_task()
  else:
    return get_tasks()

if(__name__ == '__main__'):
  app.run(debug=True)
