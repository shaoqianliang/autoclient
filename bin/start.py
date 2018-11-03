import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
os.environ['USER_SETTINGS'] = 'config.settings'

if __name__ == '__main__':
    from src import script
    script.run()