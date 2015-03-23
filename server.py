import json
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='client')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/tasks.json', methods=['GET', 'POST'])
def tasks_handler():

    with open('tasks.json', 'r') as file:
        tasks = json.loads(file.read())

    if request.method == 'POST':
        tasks.append(request.form.to_dict())

        with open('tasks.json', 'w') as file:
            file.write(json.dumps(tasks, indent=4, separators=(',', ': ')))

    return Response(json.dumps(tasks), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run(port=3000)
