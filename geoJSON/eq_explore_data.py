from pathlib import Path
import json

path = Path('eq_data/eq_data_d1_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

