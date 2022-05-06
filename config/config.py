import logging
import os

import sys
import yaml

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

configs = dict()

# parse config file
config_file = os.path.join(project_dir, 'config.yaml')
with open(config_file, 'r') as f:
    configs = yaml.load(f, Loader=yaml.SafeLoader)


# read config to variables
def get_config(key, default=None, data_type=None):
    value = os.getenv(key, configs['config'].get(key, default))
    if data_type == int:
        if value is not None:
            value = data_type(value)
    elif data_type:
        value = data_type(value)
    return value


def save_configs(configs):
    with open(config_file, 'w') as _f:
        yaml.safe_dump(configs, _f)


# set up logging config
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s.%(msecs)03d - %(name)7s %(levelname)-4s - %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',

)

logger = logging.getLogger('autolog')
