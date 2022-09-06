def get_input(param):
    return int(input(f"Please provide {param}: "))

height = get_input('height')
width = get_input('width')
# mines_count = get_input('count of mines')

while True:
    mines_count = get_input('count of mines')
    if height * width >= mines_count:
        break