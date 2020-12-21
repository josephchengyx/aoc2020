def remove_borders(tile):
    res = list()
    for i in range(1, len(tile)-1):
        row = tile[i]
        res.append(row[1:-1])
    return res
    
