import shlex
import subprocess
from multiprocessing.pool import ThreadPool
import json


def execute_async_workflow():
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
def execute_sync_workflow():
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


def main():
    pool = ThreadPool(processes=2)
    r = pool.apply_async(execute_async_workflow)
    print("main process exiting..")
    r.wait()

    # r = pool.apply_async(execute_sync_workflow)
    # pool.terminate()
    # pool.join()


if __name__ == '__main__':
    execute_sync_workflow()
