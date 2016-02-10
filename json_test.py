import json
import sys

class Levels:
    def __init__(self):
        self.level_number = 0
        self.timer= 0
        self.chip_number= 0
        self.upper_layer=[]
        self.lower_layer=[]
        self.optional_fields=[]


class level1(Levels):
    def __init__(self):
        self.level_number = 1
        self.timer= 150
        self.chip_number= 3
        self.upper_layer=[]
        self.lower_layer=[]
        self.optional_fields=[]

class level2(Levels):
    def __init__(self):
        self.level_number = 2
        self.timer= 150
        self.chip_number= 5
        self.upper_layer=[]
        self.lower_layer=[]
        self.optional_fields=[]


class EachLevel:
    def __init__(self,level_number=0,timer=0,chip_number=0,upper_layer=[],lower_layer=[],optional_fields=[]):
        self.level_number = level_number
        self.timer= timer
        self.chip_number=chip_number
        self.upper_layer= upper_layer
        self.lower_layer= lower_layer
        self.optional_fields= optional_fields

class LevelPack:
    def __init__(self):
        self.levels = []
    def add_level(self, EachLevel):
        self.levels.append(EachLevel)


def make_LevelPack_from_json(json_data):
    level_pack= LevelPack()
    for json_levels in json_data:
        level_number=json_levels["level_number"]
        timer=json_levels["timer"]
        chip_number=json_levels["chip_number"]
        upper_layer=json_levels["upper_layer"]
        lower_layer=json_levels["lower_layer"]
        optional_field=json_levels["optional_field"]

        real_level = None
        if Level["level_number"] == 1:
            real_level = level1()

        elif Level["level_number"] == 2:
            real_level = level2()
        level = EachLevel(real_level,timer,chip_number,upper_layer,lower_layer,optional_field)
        level_pack.add_level(level)
    return level_pack

level_data = LevelPack()
level1 = EachLevel(1,150,3,[],[],[])
level2 = EachLevel(2,150,5,[],[],[])
level_data.add_level(level1)
level_data.add_level(level2)


default_input_json_file = "data/cc_data.json"
default_output_dat_file = "data/cc_dat.dat"

if len(sys.argv) == 3:
    input_json_file = sys.argv[1]
    output_dat_file = sys.argv[2]
    print("Using command line args:", input_json_file, output_dat_file)
else:
    input_json_file = default_input_json_file
    output_dat_file = default_output_dat_file
    print("Unknown command line options. Using default values:", input_json_file, output_dat_file)

json_reader = open(input_json_file, "r")
json_data = json.load(json_reader)
json_reader.close()

level_pack = make_cc_data_from_json(json_data)