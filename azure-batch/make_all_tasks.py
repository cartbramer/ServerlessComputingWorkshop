from datetime import datetime

TASK_ID = "test2"

script_lines = []
tasks = 300
task_size = 5000  # Roughly one minute. 

with open("spawn_task.json") as f: 
  template = f.read()

template = template.replace("{TASK_ID}", TASK_ID)

for i in range(tasks):
  m1 = i * task_size
  m2 = (i+1) * task_size
  json = template.replace("{M1}", str(m1)).replace("{M2}", str(m2))
  filename = f"all_tasks/task-{TASK_ID}-{m1}-{m2}.json"
  with open(filename, 'w') as f:
    f.write(json)

  script_line = f"az batch task create --job-id=jobforworkshop --json-file=all_tasks/task-{TASK_ID}-{m1}-{m2}.json"
  script_lines.append(script_line)

with open("spawn-all-tasks.sh", 'w') as f:
  f.write("\n".join(script_lines))
