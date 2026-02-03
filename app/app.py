from flask import Flask, jsonify, render_template
import json, os, re, logging
from glob import glob
from collections import defaultdict

app = Flask(__name__)
DATA_DIR = "/data"

logging.basicConfig(level=logging.INFO)

def load_data_grouped():
    files = sorted(glob(os.path.join(DATA_DIR, "*.json")))
    logging.info(f"Found {len(files)} JSON files")

    runs = defaultdict(dict)

    for file in files:
        try:
            with open(file) as f:
                j = json.load(f)

            # Endpoint extrahieren (t0–t5)
            m = re.search(r't\d', j["endpoint"])
            if not m:
                logging.warning(f"No endpoint in {file}")
                continue
            ep = m.group(0)

            # Timestamp aus Dateiname
            # speedtest-2026-01-26T12-45-49-247Z.json
            ts = os.path.basename(file).replace("speedtest-", "").replace(".json", "")

            runs[ts][ep] = j["result"]

        except Exception as e:
            logging.error(f"Error loading {file}: {e}")

    logging.info(f"Built {len(runs)} runs")
    return runs

@app.route("/data")
def data():
    return jsonify(load_data_grouped())

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    logging.info("Starting Flask")
    app.run(host="0.0.0.0", port=5000)
