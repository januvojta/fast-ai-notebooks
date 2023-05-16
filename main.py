import ssl
import hydra

# test python interpreter. If it outputs LibreSSL, then you are using wrong (system) python.
print(ssl.OPENSSL_VERSION)


from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath
#
# config: str
# def init_hydra():
#     with initialize(version_base=None, config_path="../configs"):
#         config = compose(config_name="main-config.yaml")
# def get_data_path():
#     return abspath("../" + config.data.path)

@hydra.main(version_base=None, config_path="configs", config_name='main-config')
def process_data(config: DictConfig):
    """Function to process the data"""
    raw_path = abspath(config.data.test_path)
    print(f"Process data using {raw_path}")

if __name__ == '__main__':
    process_data()