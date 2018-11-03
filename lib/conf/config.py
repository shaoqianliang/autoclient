#整合config.settings和lib.conf.default_settings
#换方式导入config.settings（加到环境变量中）
import importlib
import os
from lib.conf import default_settings


class Settings:
    def __init__(self):
        # '''默认配置'''
        self.default_settings = default_settings
        for name in dir(default_settings):#dir获取模块属性，用大写来区分，设置到本地的类中
            if name.isupper():
                value = getattr(default_settings, name)
                setattr(self, name, value)
        # 自定义配置（可能存在覆盖的情况）
        self.settings_module = os.environ.get('USER_SETTINGS')
        m = importlib.import_module(self.settings_module)
        for name in dir(m):
            if name.isupper():
                value = getattr(m, name)
                setattr(self, name, value)


settings = Settings()

