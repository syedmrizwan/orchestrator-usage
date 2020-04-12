import subprocess

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

process = subprocess.Popen(['sudo', 'docker', 'run', '--network=host', '--rm', 'ubercadence/cli:master', '--domain', 'test-domain', 'workflow', 'run', '--tl', 'helloWorldGroup', '--wt', 'github.com/syedmrizwan/orchestrator/src/workflows.DemoWorkflow', '--et', '300'
                            ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = process.communicate(
    input="Hello from the other side!")
process.wait()
print(output)
print(errors)
