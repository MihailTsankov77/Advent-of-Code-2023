(day_two_part_one:= lambda x: sum(map(lambda _: _[0], filter(check_if_row_is_valid, split_to_map(x)))), day_two_part_two:=lambda x: sum(map(get_game_value, split_to_map(x))), split_to_map:= lambda x: list((int(row.split(':')[0].split('Game ')[1]), list(list((cell.split(' ')[2], int(cell.split(' ')[1]))  for cell in groups.split(',')) for groups in row.split(':')[1].split(';'))) for row in x.split('\n')), check_if_row_is_valid:= lambda game: all(map(lambda x: check_if_group_is_valid(x), game[1])), check_if_group_is_valid:= lambda group: check_config(get_group_count(arr:=list(group), 'blue'), get_group_count(arr, 'red'), get_group_count(arr, 'green')), get_group_count:= lambda group, type: sum(map(lambda x: x[1], filter(lambda x: x[0] == type, group))), check_config:= lambda blue, red, green: red<=12 and green<=13 and blue<=14, multiply:= lambda arr: next(i := iter(l)) * multiply(i) if (l := list(arr)) else 1, flatten:= lambda arr: (item for sublist in arr for item in sublist), get_game_value:=lambda game: multiply(get_max_for_color(game, color) for color in ['blue', 'red', 'green']), get_max_for_color:= lambda game, color: max(flatten(map(lambda _: _[1], filter(lambda x: x[0]==color, group)) for group in game[1])))
