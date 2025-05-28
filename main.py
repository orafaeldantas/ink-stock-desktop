
import sys
import os

# Adiciona a pasta src no sys.path para importações funcionarem
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.gui.main_window import create_main_window

if __name__ == '__main__':
    create_main_window()