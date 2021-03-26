from pathlib import Path
import json
import requests


employers = json.loads(
    Path('mock-base', 'employers.json').read_text()
)

for employer in employers['pdvs']:
    requests.post(
        'http://127.0.0.1:5000/employer',
        json=employer
    )
