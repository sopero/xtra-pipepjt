"""Running the Xetra ETL application"""

import logging
import logging.config

import yaml

def main():
    """
    entry point to run the xetra elt job
    """

    #Parsing YAML file
    config_path = '/Users/sondraperrot/Documents/pipeline_project/xtra-pipepjt/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))

    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config) #load the config as dictionary
    logger = logging.getLogger(__name__) #use name of the file
    logger.info("This is a test.")

if __name__ == '__main__':
    main()
