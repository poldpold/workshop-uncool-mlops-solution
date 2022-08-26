import json
import os
import pandas as pd
from collections import Counter
from pathlib import Path

import fire
import yaml
from loguru import logger


@logger.catch(reraise=True)
def fit(data_output_folder, fit_output_folder, fit_metrics_folder):
    base_dir = os.path.dirname(__file__) + "/.."
    
    with open(base_dir+"/params.yaml") as f:
        params = yaml.safe_load(f)["fit"]

    input_folder = base_dir + "/" + data_output_folder
    output_folder = base_dir + "/" + fit_output_folder
    
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    trades = pd.read_csv(input_folder + "/trades.csv")
    
    
    metrics = {"num_trades": len(trades)}
    
    output_metrics_folder = base_dir + "/" + fit_metrics_folder
    Path(output_metrics_folder).mkdir(parents=True, exist_ok=True)
    
    Path(base_dir+"/"+params["metrics_file"]).write_text(json.dumps(metrics, indent=4))

if __name__ == "__main__":
    fire.Fire(fit)