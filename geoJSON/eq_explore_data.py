from pathlib import Path
import json

path = Path('eq_data/eq_data_d1_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path('eq_data/cleaner_eq_data.geojson')
cleaner_contents = json.dumps(all_eq_data, indent=4)
path.write_text(cleaner_contents)
