import shlex
import subprocess
import json

# calling asynchronouslly
process = subprocess.Popen(
    ['sudo', 'docker', 'run', '--network=host', '--rm', 'ubercadence/cli:master', '--domain', 'test-domain', 'workflow',
     'start', '--wt', 'github.com/syedmrizwan/orchestrator/src/workflows.DemoWorkflow', '--tl', 'helloWorldGroup',
     '-et', '300'
     ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout, stderr)


# calling synchronouslly

command = 'sudo docker run --network=host --rm ubercadence/cli:master --domain test-domain workflow run --tl helloWorldGroup --wt github.com/syedmrizwan/orchestrator/src/workflows.DemoWorkflow --et 300'
args = shlex.split(command)
process = subprocess.Popen(args, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
# process.wait()
# print(stdout)
# print(stderr)
for line in process.stdout:
    if 'Output:' in line:
        temp = line.rstrip().replace("Output:", "").strip()
        temp = json.loads(temp)
        print "test:", temp['value2']
