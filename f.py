from tkinter import *
import re
from tkinter import ttk
import json
import os
import pyautogui
import time
import cv2
import numpy as np
import keyboard
import pygetwindow as gw
import threading
import copy


"""
LOADS DATA AND CONSTANT VARIABLES TO RAM
"""

try:
    os.mkdir("C:/autochess_data")
except OSError as error:
    pass

namelist = [
    'AA',
    'Abaddon',
    'Alchemist',
    'AM',
    'Arc',
    'Axe',
    'Bane',
    'Barathum',
    'Batrider',
    'BB',
    'BeastMaster',
    'BH',
    'Blood',
    'Brood',
    'Centaur',
    'Chaos',
    'Chen',
    'Clinkz',
    'Clock',
    'CM',
    'DarkWillow',
    'Dazzle',
    'Disruptor',
    'Doom',
    'DP',
    'DragonKnight',
    'Drow',
    'DS',
    'EarthShaker',
    'EarthSpirit',
    'Elder',
    'EmberSpirit',
    'Enchantress',
    'Enigma',
    'Grandma',
    'Grim',
    'Gyro',
    'Huskar',
    'IceDuck',
    'Invoker',
    'IO',
    'Jakiro',
    'Juggernaut',
    'KOTL',
    'Kunkka',
    'LC',
    'LD',
    'Leshrac',
    'Lich',
    'Lina',
    'Lion',
    'Luna',
    'Lycan',
    'Magnus',
    'Mars',
    'Medusa',
    'Meepo',
    'Mirana',
    'MonkeyKing',
    'Morph',
    'Naga',
    'Naix',
    'Necrophos',
    'Nevermore',
    'NP',
    'NS',
    'Nyx',
    'OD',
    'OgreMagi',
    'OmniKnight',
    'Oracle',
    'Panda',
    'Pangolier',
    'Phoenix',
    'PhuongAnh',
    'PhuongLinh',
    'Puck',
    'Pudge',
    'Pugna',
    'QOP',
    'Razor',
    'Riki',
    'Rubik',
    'SandKing',
    'SD',
    'ShadowShaman',
    'Silencer',
    'SkeletonKing',
    'SkywrathMage',
    'Sladar',
    'Slark',
    'Sniper',
    'Spectre',
    'Storm',
    'Sven',
    'TB',
    'Terrorist',
    'Tide',
    'Timber',
    'Tinker',
    'Tiny',
    'TramAnh',
    'Treant',
    'Troll',
    'Tuskar',
    'Underlord',
    'Undying',
    'Ursa',
    'Venom',
    'Viper',
    'Visage',
    'Void',
    'VoidSpirit',
    'VS',
    'Warlock',
    'Weaver',
    'WindRanger',
    'WitchDoctor',
    'WraithKing',
    'Zeus'
]

# creates Dictionary for Rank, Species, Class, and number of heroes left in Pool for creating table
RSCP_Dict = {}
RSCP_Dict = {'Barathum': ['1G', 'Chieftan', 'Assassin', 'Barathum', 45], 'Axe': ['1G', 'Orc', 'Warrior', 'Axe', 45], 'Enchantress': ['1G', 'Beast', 'Druid', 'Enchantress', 45], 'Tuskar': ['1G', 'Beast', 'Warrior', 'Tuskar', 45], 'Drow': ['1G',
 'Undad', 'Hunter', 'Drow', 45], 'BH': ['1G', 'Goblin', 'Assassin', 'BH', 45], 'Clock': ['1G', 'Goblin', 'Inventor', 'Clock', 45], 'ShadowShaman': ['1G', 'Troll', 'Shaman', 'ShadowShaman', 45], 'Tinker': ['1G', 'Goblin', 'Inventor', 'Tinker', 45], 'AM': ['1G', 'Elf', 'DemonHunter', 'AM', 45], 'Tiny': ['1G', 'Elemental', 'Warrior', 'Tiny', 45], 'Mars': ['1G', 'God', 'Warrior', 'Mars', 45], 'IceDuck': ['1G', 'Dragon', 'Mage', 'IceDuck', 45], 'CM': ['1G', 'Human', 'Mage', 'CM', 45], 'Luna': ['1G', 'Elf', 'Knight', 'Luna', 45], 'WitchDoctor': ['1G', 'Troll', 'Warlock', 'WitchDoctor', 45], 'Lion': ['2G', 'Demon', 'Wizard', 'Lion', 30], 'Batrider': ['2G', 'Troll', 'Knight', 'Batrider', 30], 'OgreMagi': ['2G', 'Ogre', 'Mage', 'OgreMagi', 30], 'BeastMaster': ['2G', 'Orc', 'Hunter', 'BeastMaster', 30], 'Juggernaut': ['2G', 'Orc', 'Warrior', 'Juggernaut', 30], 'Timber': ['2G', 'Goblin', 'Inventor', 'Timber', 30], 'Chaos': ['2G', 'Demon', 'Knight', 'Chaos', 30], 'Morph': ['2G', 'Elemental', 'Assassin', 'Morph', 30], 'NP': ['2G', 'Elf', 'Druid', 'NP', 30], 'Mirana': ['2G', 'Elf', 'Hunter', 'Mirana', 30], 'Slark': ['2G', 'Naga', 'Assassin', 'Slark',
 30], 'Dazzle': ['2G', 'Troll', 'Priest', 'Dazzle', 30], 'Sniper': ['2G', 'Dwarf', 'Hunter', 'Sniper', 30], 'Abaddon': ['2G', 'Undead', 'Knight', 'Abaddon', 30], 'Oracle': ['2G', 'God', 'Priest', 'Oracle', 30], 'Panda': ['2G', 'Pandaren', 'Monk', 'Panda', 30], 'Venom': ['3G', 'Aqir/Beast', 'Warlock', 'Venom', 25], 'OmniKnight': ['3G', 'Human', 'Knight', 'OmniKnight', 25], 'Razor': ['3G', 'Elemental', 'Mage', 'Razor', 25], 'PhuongAnh': ['3G', 'Elf', 'Assassin', 'PhuongAnh', 25], 'Treant': ['3G', 'Elf', 'Druid', 'Treant', 25], 'Sladar': ['3G', 'Naga', 'Warrior', 'Sladar', 25], 'SandKing': ['3G', 'Aqir', 'Assassin', 'SandKing', 25], 'Lycan': ['3G', 'Human/Beast', 'Warrior', 'Lycan', 25], 'TB': ['3G', 'Demon', 'DemonHunter', 'TB', 25], 'Viper': ['3G', 'Dragon', 'Assassin', 'Viper', 25], 'Nevermore': ['3G', 'Demon', 'Warlock', 'Nevermore', 25], 'LC': ['3G', 'Human', 'Knight', 'LC', 25], 'Lina': ['3G', 'Human', 'Mage', 'Lina', 25], 'Visage': ['3G', 'Dragon/Undead', 'Hunter', 'Visage', 25], 'Rubik': ['3G', 'God', 'Wizard', 'Rubik', 25], 'Meepo': ['3G', 'Kobold', 'Inventor', 'Meepo', 25], 'WindRanger': ['4G', 'Elf', 'Hunter', 'WindRanger', 15],
'Doom': ['4G', 'Demon', 'Warrior', 'Doom', 15], 'Kunkka': ['4G', 'Human', 'Warrior', 'Kunkka', 15], 'Grim': ['4G', 'Demon', 'Wizard', 'Grim', 15], 'KOTL': ['4G', 'Human', 'Mage', 'KOTL', 15], 'Necrophos': ['4G', 'Undead', 'Warlock', 'Necrophos', 15], 'Alchemist': ['4G', 'Goblin', 'Warlock', 'Alchemist', 15], 'DragonKnight': ['4G', 'Human/Dragon', 'Knight', 'DragonKnight', 15], 'Medusa': ['4G', 'Naga', 'Hunter', 'Medusa', 15], 'LD': ['4G', 'Beast', 'Druid', 'LD', 15], 'Chen': ['4G', 'Orc', 'Priest', 'Chen', 15], 'Nyx': ['4G', 'Aqir', 'Assassin', 'Nyx', 15], 'Brood': ['4G', 'Aqir', 'Hunter', 'Brood', 15], 'EarthShaker': ['4G', 'Chieftan', 'Shaman', 'EarthShaker', 15], 'Disruptor': ['5G', 'Orc', 'Shaman', 'Disruptor', 10], 'Gyro': ['5G', 'Dwarf', 'Inventor', 'Gyro', 10], 'Tide': ['5G', 'Naga', 'Hunter', 'Tide', 10], 'Enigma': ['5G', 'Elemental', 'Warlock', 'Enigma', 10], 'Terrorist': ['5G', 'Goblin', 'Inventor', 'Terrorist', 10], 'Elder': ['5G', 'God/Chieftan', 'Druid', 'Elder', 10], 'Sven': ['5G', 'Demon', 'Warrior', 'Sven', 10], 'Zeus': ['5G', 'God', 'Mage', 'Zeus', 10], 'QOP': ['5G', 'Demon', 'Assassin', 'QOP', 10], 'TramAnh': ['5G', 'Elf', 'Assassin', 'TramAnh', 10], 'MonkeyKing': ['5G', 'Beast', 'Monk', 'MonkeyKing', 10], 'Invoker': ['5G', 'Elf', 'Mage', 'Invoker', 10], 'Huskar': ['5G', 'Troll', 'Warrior', 'Huskar', 10], 'Jakiro': ['5G', 'Dragon', 'Mage', 'Jakiro', 10], 'Snapfire': ['5G', 'Goblin', 'Knight', 'Snapfire', 10]}

# Loads all hero icons to memory
count2 = 0
hero_icon_dict = {}
for file in os.listdir('G:/icon'):
    file_path = "G:/icon/" + file
    hero_icon_dict[namelist[count2]] = cv2.imread(file_path)
    count2 +=1

# Loads level icons to memory
level_dict = {}
level_dict[""] = cv2.imread("G:/level/1.png", 0)
level_dict["2"] = cv2.imread("G:/level/2.png", 0)
level_dict["3"] = cv2.imread("G:/level/3.png", 0)

TIMESLEEP = 0.2

HERO_ICON_WIDTH = 33
FIRST_X_START = 711
FIRST_X_END = 744

SECOND_X_START = FIRST_X_START + HERO_ICON_WIDTH
SECOND_X_END = FIRST_X_END + HERO_ICON_WIDTH

THIRD_X_START = SECOND_X_START + HERO_ICON_WIDTH + 1
THIRD_X_END = SECOND_X_END + HERO_ICON_WIDTH + 1

FOURTH_X_START = THIRD_X_START + HERO_ICON_WIDTH
FOURTH_X_END = THIRD_X_END + HERO_ICON_WIDTH

FIFTH_X_START = FOURTH_X_START + HERO_ICON_WIDTH
FIFTH_X_END = FOURTH_X_END + HERO_ICON_WIDTH

SIXTH_X_START = FIFTH_X_START + HERO_ICON_WIDTH + 1
SIXTH_X_END = FIFTH_X_END + HERO_ICON_WIDTH + 1

SEVENTH_X_START = SIXTH_X_START + HERO_ICON_WIDTH
SEVENTH_X_END = SIXTH_X_END + HERO_ICON_WIDTH

EIGHTH_X_START = SEVENTH_X_START + HERO_ICON_WIDTH
EIGHTH_X_END = SEVENTH_X_END + HERO_ICON_WIDTH

NINTH_X_START = EIGHTH_X_START + HERO_ICON_WIDTH + 1
NINTH_X_END = EIGHTH_X_END + HERO_ICON_WIDTH + 1

TENTH_X_START = NINTH_X_START + HERO_ICON_WIDTH
TENTH_X_END = NINTH_X_END + HERO_ICON_WIDTH


PLAYER_DISTANCE = 88
FIRST_Y_START = 221
FIRST_Y_END = 256

SECOND_Y_START = FIRST_Y_START + PLAYER_DISTANCE
SECOND_Y_END = FIRST_Y_END + PLAYER_DISTANCE

THIRD_Y_START = SECOND_Y_START + PLAYER_DISTANCE - 1
THIRD_Y_END = SECOND_Y_END + PLAYER_DISTANCE - 1

FOURTH_Y_START = THIRD_Y_START + PLAYER_DISTANCE - 1
FOURTH_Y_END = THIRD_Y_END + PLAYER_DISTANCE - 1

FIFTH_Y_START = FOURTH_Y_START + PLAYER_DISTANCE
FIFTH_Y_END = FOURTH_Y_END + PLAYER_DISTANCE

SIXTH_Y_START = FIFTH_Y_START + PLAYER_DISTANCE
SIXTH_Y_END = FIFTH_Y_END + PLAYER_DISTANCE

SEVENTH_Y_START = SIXTH_Y_START + PLAYER_DISTANCE - 1
SEVENTH_Y_END = SIXTH_Y_END + PLAYER_DISTANCE - 1

EIGHTH_Y_START = SEVENTH_Y_START + PLAYER_DISTANCE - 1
EIGHTH_Y_END = SEVENTH_Y_END + PLAYER_DISTANCE - 1

X_COORDINATES_START = (FIRST_X_START, SECOND_X_START, THIRD_X_START, FOURTH_X_START, FIFTH_X_START, SIXTH_X_START, SEVENTH_X_START, EIGHTH_X_START, NINTH_X_START, TENTH_X_START)
X_COORDINATES_END = (FIRST_X_END, SECOND_X_END, THIRD_X_END, FOURTH_X_END, FIFTH_X_END, SIXTH_X_END, SEVENTH_X_END, EIGHTH_X_END, NINTH_X_END, TENTH_X_END)
Y_COORDINATES_START = (FIRST_Y_START, SECOND_Y_START, THIRD_Y_START, FOURTH_Y_START, FIFTH_Y_START, SIXTH_Y_START, SEVENTH_Y_START, EIGHTH_Y_START)
Y_COORDINATES_END = (FIRST_Y_END, SECOND_Y_END, THIRD_Y_END, FOURTH_Y_END, FIFTH_Y_END, SIXTH_Y_END, SEVENTH_Y_END, EIGHTH_Y_END)

LEVEL_ICON_HEIGHT = 7

LEVEL_AND_HERO_ICON_HEIGHT = 42

ICON_FIRST_ROI = (0, LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_SECOND_ROI = (LEVEL_AND_HERO_ICON_HEIGHT, 2*LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_THIRD_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*2, 3*LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_FOURTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*3, 4*LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_FIFTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*4, 5*LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_SIXTH_ROI = (0, LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_SEVENTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT, 2*LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_EIGHTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*2, 3*LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_NINETH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*3, 4*LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_TENTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT*4, 5*LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)

ROI_TUPLE = (ICON_FIRST_ROI, ICON_SECOND_ROI, ICON_THIRD_ROI, ICON_FOURTH_ROI, ICON_FIFTH_ROI, ICON_SIXTH_ROI, ICON_SEVENTH_ROI, ICON_EIGHTH_ROI, ICON_NINETH_ROI, ICON_TENTH_ROI)

to_show_list = []
on_stage_list = []


"""
DEFINES CLASSES AND FUNCTIONS FOR TKINTER 
"""




# SORTS TREEVIEW COLUMN
def treeview_sort_column(treeview: ttk.Treeview, col, reverse: bool):
    """
    to sort the table by column when clicking in column
    """
    try:
        data_list = [
            (int(treeview.set(k, col)), k) for k in treeview.get_children("")
        ]
    except Exception:
        data_list = [(treeview.set(k, col), k) for k in treeview.get_children("")]

    data_list.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(data_list):
        treeview.move(k, "", index)

    # reverse sort next time
    treeview.heading(
        column=col,
        text=col,
        command=lambda col3=col: treeview_sort_column(
            treeview, col3, not reverse),)



# MAKES TKINTER COMMANDS TO USE THREADS
def thread(function, arg = None):
    if arg == None:
        x = threading.Thread(target=function)
        x.start()
    else:
        x = threading.Thread(target=function(arg))
        x.start()


style = ttk.Style()

def fixed_map(option):
    return [elm for elm in style.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]

style.map("Treeview",
          foreground=fixed_map("foreground"),
          background=fixed_map("background"))

"""
DEFINES FUNCTIONS FOR BUTTONS
"""

# DEFINES WHAT SCAN BUTTON DOES
def Scan():
    # try:
    #     dota = gw.getWindowsWithTitle("Dota 2")[0]
    #     dota.activate()
    # except IndexError as error:
    #     pass
    # time.sleep(TIMESLEEP)
    # pyautogui.click(x=348, y=798)
    # pyautogui.click(x=348, y=798)

    # os.chdir("C:/autochess_data")
    # screenshot = pyautogui.screenshot()
    # screenshot = np.asarray(screenshot)
    # player_status_list = [screenshot[438:449, 1705:1754], screenshot[525:536, 1705:1754], screenshot[613:624, 1705:1754], screenshot[701:712, 1705:1754], screenshot[788:799, 1705:1754],
    #                       screenshot[875:886, 1705:1754]]
    #
    # failed_icon = cv2.imread("C:/autochess_data/failed_icon.png")
    # transparent_failed_icon = cv2.imread("C:/autochess_data/transparent_failed_icon.png")
    #
    # num_of_lost_players = 0
    # for i in range(0, len(player_status_list)):
    #     if max(cv2.matchTemplate(player_status_list[i], failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8 or max(
    #             cv2.matchTemplate(player_status_list[i], transparent_failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8:
    #         num_of_lost_players = 6 - i
    #         break
    #
    # keyboard.press_and_release("f3")
    # time.sleep(0.5)
    # on_stage_heroes = pyautogui.screenshot()
    # keyboard.press_and_release("f3")
    # # on_stage_heroes.save("on_stage_heroes.png")
    # time.sleep(0.3)
    #
    # count = 0
    # pyautogui.click(x=1602, y=233)
    # pyautogui.click(x=1602, y=233)
    # time.sleep(TIMESLEEP)
    # img = pyautogui.screenshot(region=(527, 619, 848, 212))
    # count += 1
    # img.save(f"{count}.jpg")
    #
    # pyautogui.click(x=1602, y=320)
    # pyautogui.click(x=1602, y=320)
    # time.sleep(TIMESLEEP)
    # img = pyautogui.screenshot(region=(527, 619, 848, 212))
    # count += 1
    # img.save(f"{count}.jpg")
    #
    # if num_of_lost_players < 6:
    #     pyautogui.click(x=1602, y=409)
    #     pyautogui.click(x=1602, y=409)
    #     time.sleep(TIMESLEEP)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # if num_of_lost_players < 5:
    #     pyautogui.click(x=1602, y=497)
    #     pyautogui.click(x=1602, y=497)
    #     time.sleep(TIMESLEEP)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # if num_of_lost_players < 4:
    #     pyautogui.click(x=1602, y=586)
    #     pyautogui.click(x=1602, y=586)
    #     time.sleep(TIMESLEEP)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # if num_of_lost_players < 3:
    #     pyautogui.click(x=1602, y=670)
    #     pyautogui.click(x=1602, y=670)
    #     pyautogui.moveTo(x=1546, y=620)
    #     time.sleep(0.5)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # if num_of_lost_players < 2:
    #     pyautogui.click(x=1602, y=758)
    #     pyautogui.click(x=1602, y=758)
    #     pyautogui.moveTo(x=1546, y=708)
    #     time.sleep(0.5)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # if num_of_lost_players < 1:
    #     pyautogui.click(x=1602, y=844)
    #     pyautogui.click(x=1602, y=844)
    #     pyautogui.moveTo(x=1546, y=794)
    #     time.sleep(0.5)
    #     img = pyautogui.screenshot(region=(527, 619, 848, 212))
    #     count += 1
    #     img.save(f"{count}.jpg")
    # else:
    #     img = cv2.imread("C:/autochess_data/Lost.png")
    #     count += 1
    #     cv2.imwrite(f"{count}.jpg", img)
    #
    # os.chdir("G:/darknet/")
    # os.system("G:\darknet/darknet.exe detector test G:\darknet/obj.data G:/darknet/thresh_cfg.cfg G:\darknetsave/yolov4-obj_last_25.weights -ext_output -dont_show -out result.json < data/train.txt")
    #
    # f = open("G:/darknet/result.json")
    # data = json.load(f)

    all_chess_pieces_list = [[],[],[],[],[],[],[],[]]
    # for i in range(8):
    #     for hero in data[i]["objects"]:
    #         all_chess_pieces_list[i].append(hero["name"])

    temp_on_stage_list = [[],[],[],[],[],[],[],[]]
    os.chdir("C:/autochess_data/")
    count3 = 0
    num_of_lost_players = 0
    for i in range(0, 80-num_of_lost_players*10):
        if i % 10 == 0:
            count3 = 0 + int(i / 10)

        img = cv2.imread("C:/autochess_data/on_stage_heroes.png")
        grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hero_level = ""
        level_icon_template = grayed_img[
                              Y_COORDINATES_END[count3] + 1:Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT,
                              X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
        for level in level_dict:
            res = cv2.matchTemplate(level_dict[level], level_icon_template, cv2.TM_CCOEFF_NORMED)
            if max(res) > 0.7:
                hero_level = level
                break

        template = img[Y_COORDINATES_START[count3]:Y_COORDINATES_END[count3],
                   X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
        all_matches = []
        for hero_name in namelist:
            res = cv2.matchTemplate(hero_icon_dict[hero_name], template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.65)
            if loc[0].size > 0:
                all_matches.append((hero_name, max(res)))

        all_matches = sorted(all_matches, key=lambda match: match[1])
        if len(all_matches) > 0:
            all_chess_pieces_list[count3].append(all_matches[-1][0] + hero_level)
            temp_on_stage_list[count3].append((all_matches[-1][0] + hero_level, Y_COORDINATES_START[count3], Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT, X_COORDINATES_START[i % 10], X_COORDINATES_END[i % 10]))

    flat_list = [item for sublist in all_chess_pieces_list for item in sublist]
    treeview.delete(*treeview.get_children())
    Dict = copy.deepcopy(RSCP_Dict)

    for hero in flat_list:
        if hero.endswith("2"):
            Dict[hero[:-1]][4] -= 3
        elif hero.endswith("3"):
            Dict[hero[:-1]][4] -= 9
        else:
            Dict[hero][4] -= 1
    count5 = 0
    for key in Dict:
        tag = Dict[key][0]
        treeview.insert(parent="", index='end', iid=count5, text='', values=(
        Dict[key][0], Dict[key][1], Dict[key][2], Dict[key][3], Dict[key][4]), tags=tag)
        count5 += 1

    global to_show_list
    to_show_list = all_chess_pieces_list
    global on_stage_list
    on_stage_list = temp_on_stage_list





# DEFINES WHAT SHOW PREDICTIONS BUTTON DOES
def show_predictions():
    HEIGHT = 212
    WIDTH = 848
    COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255), (0, 0, 255), (255, 255, 255),
              (125, 0, 255), (255, 0, 125), (125, 255, 0), (0, 255, 125), (0, 125, 255), (255, 125, 0), (125, 75, 0),
              (0, 75, 125), (0, 125, 75), (75, 125, 0), (75, 0, 125), (125, 0, 75)]
    f = open("G:/darknet/result.json")
    data = json.load(f)
    global on_stage_list
    on_stage_img = cv2.imread("C:/autochess_data/on_stage_heroes.png")
    first_half = np.zeros((0, 1160, 3), dtype=np.uint8)
    second_half = np.zeros((0, 1160, 3), dtype=np.uint8)
    os.chdir("C:/autochess_data")
    for i in range(0, len(data)):
        img = cv2.imread(f"C:/autochess_data/{i+1}.jpg")
        for hero in data[i]['objects']:
            x_start = round(
                hero["relative_coordinates"]["center_x"] * WIDTH - hero["relative_coordinates"]["width"] * WIDTH / 2)
            x_end = round(
                hero["relative_coordinates"]["center_x"] * WIDTH + hero["relative_coordinates"]["width"] * WIDTH / 2)
            y_start = round(
                hero["relative_coordinates"]["center_y"] * HEIGHT - hero["relative_coordinates"]["height"] * HEIGHT / 2)
            y_end = round(
                hero["relative_coordinates"]["center_y"] * HEIGHT + hero["relative_coordinates"]["height"] * HEIGHT / 2)
            cv2.rectangle(img, (x_start, y_start), (x_end, y_end), COLORS[int(hero['class_id']) % len(COLORS)], 1)
            cv2.putText(img, hero['name'], (x_start, y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                        COLORS[int(hero['class_id']) % len(COLORS)], 1)
            cv2.putText(img, f"player{i+1}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        count = 0
        bg = np.zeros((212, 312, 3), dtype=np.uint8)
        bg[0:210,:] = 255
        for hero in on_stage_list[i]:
            icon = on_stage_img[hero[1]:hero[2]-1, hero[3]:hero[4]]
            bg[ROI_TUPLE[count][0]:ROI_TUPLE[count][1], ROI_TUPLE[count][2]:ROI_TUPLE[count][3]] = icon
            cv2.putText(bg, hero[0], (ROI_TUPLE[count][2] + HERO_ICON_WIDTH, ROI_TUPLE[count][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            count +=1
        img = cv2.hconcat([bg, img])

        if i in range (0,4):
            first_half = cv2.vconcat([first_half, img])
        if i in range (4,8):
            second_half = cv2.vconcat([second_half, img])


    all_predictions = cv2.hconcat([first_half, second_half])
    cv2.imwrite("C:/autochess_data/all_predictions.jpg", all_predictions)
    os.system("C:/autochess_data/all_predictions.jpg")



def show_lineups():
    global to_show_list
    print(to_show_list)


# DEFINES WHAT HAPPENS WHEN DOUBLE CLICK ON CELL
def on_double_click(event):
    col = int(treeview.identify_column(event.x)[1])
    item_id = event.widget.focus()
    print(event.widget.item(item_id)['values'][col-1])


if __name__ == '__main__':
    root = Tk()
    root.title('Autochess Lineup and Probability Tracker')
    root.geometry("500x900")

    style.map('Treeview', background=[('selected', 'white')], foreground=[('selected', 'black')])

    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11), background="gray21") # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 12,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    columns = ['R', 'Species', 'Class', 'Name', 'N']
    treeview = ttk.Treeview(root, columns=columns, show='headings', style="mystyle.Treeview", height=20)
    for col in columns:
        treeview.heading(col, text=col, anchor="w", command=lambda col3 = col:treeview_sort_column(treeview, col3, False))
    treeview.column('R', anchor='w', width=25)
    treeview.column('Species', anchor='w', width=90)
    treeview.column('Class', anchor='w', width=90)
    treeview.column('Name', anchor='w', width=93)
    treeview.column('N', anchor='w', width=24)


    count1 = 0
    for key in RSCP_Dict:
        tag = RSCP_Dict[key][0]
        treeview.insert(parent="", index='end', iid=count1, text='', values=(RSCP_Dict[key][0], RSCP_Dict[key][1], RSCP_Dict[key][2], RSCP_Dict[key][3], RSCP_Dict[key][4]), tags=tag)
        count1 +=1

    treeview.bind("<Double-Button-1>", on_double_click)

    treeview.tag_configure('1G', foreground="white")
    treeview.tag_configure('2G', foreground="gray63")
    treeview.tag_configure('3G', foreground="dodgerblue")
    treeview.tag_configure('4G', foreground="magenta2")
    treeview.tag_configure('5G', foreground="gold")



    treeview.grid(row=0,column=1)

    check_lineups = Button(root, text="Scan", font=("Helvetica", 24), padx=12, pady=12, command= lambda: thread(Scan))
    check_lineups.grid(row=1,column=0, columnspan=2 , padx=50, pady=(10, 60))

    showpredictions = Button(root, text="Show Predictions", command= lambda: thread(show_predictions))
    showpredictions.grid(row=2,column=0)

    show_lineups = Button(root, text="Show Lineups", command=show_lineups)
    show_lineups.grid(row=2,column=1)

    root.mainloop()