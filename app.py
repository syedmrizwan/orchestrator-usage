import subprocess

process = subprocess.Popen(
    ['sudo', 'docker', 'run', '--network=host', '--rm', 'ubercadence/cli:master', '--domain', 'test-domain', 'workflow',
     'start', '--wt', 'github.com/syedmrizwan/orchestrator/src/workflows.DemoWorkflow', '--tl', 'helloWorldGroup',
     '-et', '300'
     ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout, stderr)
