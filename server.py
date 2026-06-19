

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    empty__list = []
    for element in birds: 
        if element == "African" or element == "Toulouse" or element == "Pilgrim" or element == "Roman Tufted" or element == "Steinbacher":
            pass
        else: 
            empty__list.append(element)
    return empty__list


print(goose_filter(geese))