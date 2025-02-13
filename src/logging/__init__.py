import logging
from datetime import datetime
import os




#log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#logging directory name
log_dir = "logs"


#full path to the log file
logs_path = os.path.join(os.getcwd(),log_dir,LOG_FILE)

#create log directory if it doesn't exist logs/log_file_path
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(filename=logs_path,
                    format="%(asctime)s %(levelname)s %(filename)s %(message)s",
                    level=logging.INFO)
