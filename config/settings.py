MODE = 'agent'
SSH_USER = 'root'
SSH_PORT = 22
SSH_PWD = 123
SSH_KEY = b'......'
#参照django的中间件(不过django列表形式)
PLUGINS_DICT = {
    'basic': "src.plugins.basic.Basic",
    'board': "src.plugins.board.Board",
    'cpu': "src.plugins.cpu.Cpu",
    'disk': "src.plugins.disk.Disk",
    'memory': "src.plugins.memory.Memory",
    'nic': "src.plugins.nic.Nic",
}