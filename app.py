from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Shivani S S"
    username = os.getenv("USERNAME") or os.getenv("USER")

    ist = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Hello {name} ({username})!
    Current IST time: {time_now}

    htop output:
    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)