import configparser
import pathlib


def api_key_utils():

    # https://www.pythonanywhere.com/forums/topic/30771/#id_post_100134
    config_path = pathlib.Path(__file__).parent.absolute() / "config.ini"
    
    # Crea un objeto ConfigParser
    config = configparser.ConfigParser()
    # Lee el archivo de configuración
    # config.read('config.ini')
    config.read(config_path)

    # Obtén los valores de latitud, longitud y clave API del archivo de configuración config.ini
    # lat = config.getfloat('WeatherAPI', 'lat')
    # lon = config.getfloat('WeatherAPI', 'lon')
    api_key = config.get('WeatherAPI', 'api_key')

    # Devuelve los valores
    # return lat, lon, api_key
    return api_key
