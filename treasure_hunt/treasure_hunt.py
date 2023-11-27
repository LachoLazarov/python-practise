azara_list = [
    ("Amethyst Octopus", "1F"), ("Angry Monkey Figurine", "5B"), ("Antique Glass Fishnet Float", "3D"),
    ("Brass Spyglass", "4B"), ("Carved Wooden Elephant", "8C"), ("Crystal Crab", "6A"), ("Glass Starfish", "6D"),
    ("Model Ship in Large Bottle", "8A"), ("Pirate Flag", "7F"), ("Robot Parrot", "1C"),
    ("Scrimshawed Whale Tooth", "2A"), ("Silver Seahorse", "4E"), ("Vintage Pirate Hat", "7E"),
]

rui_list = [
    ("Seaside Cottages", ("1", "C"), "Blue"), ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
    ("Deserted Docks", ("2", "A"), "Blue"), ("Spiky Rocks", ("3", "D"), "Yellow"),
    ("Abandoned Lighthouse", ("4", "B"), "Blue"), ("Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
    ("Stormy Breakwater", ("5", "B"), "Purple"), ("Old Schooner", ("6", "A"), "Purple"),
    ("Tangled Seaweed Patch", ("6", "D"), "Orange"), ("Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
    ("Windswept Hilltop (Island of Mystery)", ("7", "E"), "Orange"), ("Harbor Managers Office", ("8", "A"), "Purple"),
    ("Foggy Seacave", ("8", "C"), "Purple")
]

def get_coordinate(treasure_record):
    return treasure_record[1]

def convert_coordinate(coordinate):
    return (coordinate[:-1], coordinate[-1])

def compare_records(azara_record, rui_record):
    azara_coordinate = get_coordinate(azara_record)
    azara_coordinate = convert_coordinate(azara_coordinate)
    rui_coordinate = convert_coordinate(rui_record[1])
    return azara_coordinate == rui_coordinate

for azara_record in azara_list:
    for rui_record in rui_list:
        result = compare_records(azara_record, rui_record)
        print(f"Azara: {azara_record}, Rui: {rui_record}, Result: {result}")

