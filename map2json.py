'''
Use https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57 to create imagenet_class_index.json
'''

import json

def map2json(txt_path, json_path):
    with open(txt_path, "r") as f:
        lines = f.readlines()
    
    label_map = {}
    for line in lines:
        label, id, name = line.strip().split(" ")
        label_map[id] = [label, name]
    
    with open(json_path, "w") as f:
        json.dump(label_map, f, indent=4)

# Example usage
txt_path = "./map_clsloc.txt"
json_path = "./imagenet_class_index.json"
map2json(txt_path, json_path)