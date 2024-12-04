from todoist_api_python.api import TodoistAPI
import argparse
import os


def get_tasks(tasks_filter='',api_token=''):
    outputs = {}
    api = TodoistAPI(api_token)
    try:
        tasks = api.get_tasks(filter=tasks_filter)
        tasks.sort(key=lambda a: a.due.date)
        for task in tasks:
            if task.due.date not in outputs:
                outputs[task.due.date] = []
            if task.is_completed:
                outputs[task.due.date].append('    - (X) {}\n'.format(task.content))
            else:
                outputs[task.due.date].insert(0,'    - () {}\n'.format(task.content))
    except Exception as error:
        print("Error:")
        print(error)
    
    output_text = ''
    for date in outputs:
        output_text += '[{}]:\n'.format(date)
        for task in outputs[date]:
            output_text += task
    
    return output_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', dest='tasks_filter', default='', type=str, help='Custom filter.')
    args = parser.parse_args()
    print(get_tasks(args.tasks_filter, os.environ['TODOIST_API_TOKEN']))
