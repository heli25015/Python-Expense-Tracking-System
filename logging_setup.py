import logging

def setup_logger(name, log_file = 'server.log', level = logging.DEBUG):
    #create custom logger
    logger = logging.getLogger(name)

    #configure custom logger
    logger.setLevel(level) #can also do via basic config or an explicit method like this
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger