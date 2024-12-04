from flask import Flask, request, jsonify, send_from_directory
import xml.etree.ElementTree as ET

app = Flask(__name__)
XML_FILE = "tasks.xml"

# Helper function to read XML file
def read_tasks():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    tasks = []
    for task in root.findall('task'):
        tasks.append({
            'id': task.find('id').text,
            'name': task.find('name').text,
            'start_date': task.find('start_date').text,
            'end_date': task.find('end_date').text,
            'progress': task.find('progress').text
        })
    return tasks

# Route to fetch tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks)

# Route to update tasks
@app.route('/tasks', methods=['POST'])
def update_tasks():
    data = request.json
    root = ET.Element('tasks')
    for task in data:
        task_elem = ET.SubElement(root, 'task')
        ET.SubElement(task_elem, 'id').text = task['id']
        ET.SubElement(task_elem, 'name').text = task['name']
        ET.SubElement(task_elem, 'start_date').text = task['start_date']
        ET.SubElement(task_elem, 'end_date').text = task['end_date']
        ET.SubElement(task_elem, 'progress').text = task['progress']
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)
    return jsonify({'message': 'Tasks updated successfully'})

# Serve frontend files
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)