'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    parsed_list = [] #make the list we will eventually return
    
    # Split different packaging levels
    levels = packaging_data.split(' / ') #split the string by the '/' to get the different quantities and containers
    
    for i in levels:
        parts = i.split(' in ')
        if len(parts) == 2: #if two components
            quantity_item, container = parts 
            quantity_item_parts = quantity_item.split()
            container_parts = container.split()
            
            if len(quantity_item_parts) == 2 and len(container_parts) == 2:
                quantity1, item1 = quantity_item_parts
                quantity2, item2 = container_parts
                
                parsed_list.append({item1: int(quantity1)})#add new entry to the list of the quantity and item
    
    # Add the outermost container
    if len(container_parts) == 2: #checking to see if container and quantity
        parsed_list.append({item2: int(quantity2)})
    
    return parsed_list #return the list



def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    #make a counter variable
    count = 1
    
    # iterate through the list to multiply all quantities together
    for item in package:
        count *= list(item.values())[0]  #item.values() returns all the values in the list to extract and multiply the quantity
    return count #returns the counter variable


        


def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces
    '''
    if package:
        first_item = package[0]  # Get the first dictionary
        return list(first_item.keys())[0]  # Return the first key (unit name)
    return ""  # Return an empty string if the list is empty
    
    

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")