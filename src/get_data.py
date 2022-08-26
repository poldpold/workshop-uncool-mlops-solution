import json
import os
import pandas as pd
from collections import Counter
from pathlib import Path

import fire
import yaml
from loguru import logger


@logger.catch(reraise=True)
def get_data(output_folder):
    base_dir = os.path.dirname(__file__) + "/.."
    
    with open(base_dir+"/params.yaml") as f:
        params = yaml.safe_load(f)["data"]

    output_folder = base_dir+"/"+output_folder
    
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    metrics = Counter()
    metrics["something"] += 1
    
    logger.info(f"\nSome log.")

    trades = pd.DataFrame(dict(ops_code=["WN COMDTY 1", "CTUSD30Y"], start_time=pd.Timestamp("2022-08-08"), dayfrac=1, quantity=100000, quantity_units="dv01_usd"))
    
    trades_file = output_folder + "/trades.csv"
    trades.to_csv(trades_file)

    metrics["num_trades"] += len(trades)
    
    Path(base_dir+"/"+params["metrics_file"]).write_text(json.dumps(metrics, indent=4))


if __name__ == "__main__":
    fire.Fire(get_data)