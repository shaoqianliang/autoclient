from config import settings
import importlib
import traceback


class PluginManage:

    def __init__(self, hostname=None):
            self.hostname = hostname
            self.plugin_dict = settings.PLUGINS_DICT
            self.mode = settings.MODE
            if self.mode == 'SSH':
                self.ssh_user = settings.SSH_USER
                self.pwd = settings.SSH_PWD