import boolfunc as bf

# F = 01101001
func = [0, 1, 1, 0, 1, 0, 0, 1]
vars = ([0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1])
bf.print_info(bf.truth_table(vars, func),func)
