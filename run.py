import subprocess
import requests
import paramiko

# v = subprocess.getoutput('ipconfig')
# response = requests.post('http://127.0.0.1:8000/asset.html', data={'目录': v})
# print(response.text)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.100', port=22, username='admin', password='123')
stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout.read())
ssh.close()
