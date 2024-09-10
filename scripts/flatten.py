import json
import os


name = "players"

def flatten_file(name):
    data = []
    old_path = f"text2sql/data/esports_data/vct-challengers/{name}/{name}.json"
    new_path = f"text2sql/data/esports_data/vct-challengers/{name}/{name}_flat.json"
    with open(old_path, encoding="utf8") as f:
        data = json.load(f)


    with open(new_path, "w", encoding="utf8") as f2:
        for entry in data:
            f2.write(json.dumps(entry) + "\n")
    
    os.remove(old_path)
    os.rename(new_path, old_path)



for i in ["players", "teams", "leagues", "tournaments", "mapping_data"]:
    flatten_file(i)