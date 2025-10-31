# Thanos is looking for the six Infinity Stones. Each stone has a unique name and color:
# Space Stone: Blue
# Mind Stone: Yellow
# Reality Stone: Red
# Power Stone: Purple
# Time Stone: Green
# Soul Stone: Orange
#
# However, Thanos is colorblind. He asks you to write a program that receives the name of a stone
# and outputs the color of that stone.

stone_name = input("Enter Stone Name: ").lower()

match stone_name:
    case "space":
        print(f'The color of the "{stone_name}" stone is "Blue".')
    case "mind":
        print(f'The color of the "{stone_name}" stone is "Yellow".')
    case "reality":
        print(f'The color of the "{stone_name}" stone is "Red".')
    case "power":
        print(f'The color of the "{stone_name}" stone is "Purple".')
    case "time":
        print(f'The color of the "{stone_name}" stone is "Green".')
    case "soul":
        print(f'The color of the "{stone_name}" stone is "Orange".')