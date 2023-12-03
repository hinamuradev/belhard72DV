import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def get_tasks_for_build(build_name, builds_data, tasks_data):
    build_tasks = builds_data.get(build_name, [])
    all_tasks = []

    for task_name in build_tasks:
        task_info = tasks_data.get(task_name, {})
        task_list = [task_name]

        subtasks = task_info.get('subtasks', [])
        while subtasks:
            subtask_name = subtasks.pop(0)
            task_list.append(subtask_name)
            subtasks.extend(tasks_data[subtask_name].get('subtasks', []))

        all_tasks.extend(task_list)

    return all_tasks

# Загрузка данных из YAML файлов
builds_data = load_yaml('builds.yaml')
tasks_data = load_yaml('tasks.yaml')

# Пример использования для билда "forward_interest"
build_name = 'forward_interest'
build_tasks = get_tasks_for_build(build_name, builds_data, tasks_data)

# Вывод списка задач для выполнения билда
print(f"Билд - {build_name}")
print("Список задач:")
for task in build_tasks:
    print(task)
