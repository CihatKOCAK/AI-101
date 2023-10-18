import configparser
import os
# Yapılandırma dosyasını oluşturun ve verileri kaydedin
config = configparser.ConfigParser()
config['Settings'] = {
    'debug': True,
    'secret_key': 'my_secret_key',
    'max_users': 100
}
init_path = os.path.join(os.getcwd(), "python","part_II", "config.ini")
with open(init_path, 'w') as configfile:
    config.write(configfile)

# Yapılandırma dosyasını okuyun
config = configparser.ConfigParser()
config.read(init_path)

# Ayarları kullanın
debug_mode = config['Settings']['debug']
secret_key = config['Settings']['secret_key']
max_users = config.getint('Settings', 'max_users')

print(f'Debug Mode: {debug_mode}')
print(f'Secret Key: {secret_key}')
print(f'Max Users: {max_users}')