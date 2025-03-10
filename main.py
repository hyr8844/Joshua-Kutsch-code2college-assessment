#Peusdo code:

    #Define restuarnat_tables as a 2D list containing:
        #- Row0: Table names with capacities
        #- Other rows: Timeslots availibility('o' == free, 'x' == occupied)

    #Function list_free tables(tables, timeslot):
        #return all tables where tables[timeslot][column] == 'o'

    #function find_table_forr_party(tables, timeslot, party_size):
        #return the first free table where capacity >= party_sizem, else return none

    #function find_all_tables_for_party(tables, timeslot, party_size):
        #return all free tables where capacity >= party_size

    #function find_combined_tables_for_party(tables, timeslot, party_size):
        #return ajacent free tables where combined capacity >= party_size

    #function user_message(free_tables, combined_tables, party_size, timeslot):
        #if no tables avalible:
            #retrun "Sorry, no tables are free at this time"

    #Main program:
    #Set timeslt, party_size from the users input
    #call all functions to check the availibility 
    #print/display if avalilble or not

restaurant_tables = [
    [0,      'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,      'o',      'o',      'o',      'o',      'x',      'o'],
    [2,      'o',      'o',      'x',      'o',      'o',      'x'],
    [3,      'x',      'o',      'o',      'x',      'o',      'o'],
]

def list_free_tables(tables, timeslot):
    # Return a list of tables available in a given timeslot
    return [tables[0][col] for col in range(1, len(tables[0])) if tables[timeslot][col] == 'o']

def find_table_for_party(tables, timeslot, party_size):
    # Find a table that can hold the party size
    for col in range(1, len(tables[0])):
        table_info = tables[0][col]
        capacity = int(table_info.split('(')[1].rstrip(')'))
        if tables[timeslot][col] == 'o' and capacity >= party_size:
            return table_info
    return None

def find_all_tables_for_party(tables, timeslot, party_size):
    # Return all tables that can hold the party size
    return [tables[0][col] for col in range(1, len(tables[0]))
            if tables[timeslot][col] == 'o' and int(tables[0][col].split('(')[1].rstrip(')')) >= party_size]

def find_combined_tables_for_party(tables, timeslot, party_size):
    # Find a combination of two tables that together can seat the party
    available_combinations = []
    for col in range(1, len(tables[0]) - 1):
        table1_info, table2_info = tables[0][col], tables[0][col + 1]
        capacity1, capacity2 = int(table1_info.split('(')[1].rstrip(')')), int(table2_info.split('(')[1].rstrip(')'))

        if tables[timeslot][col] == 'o' and tables[timeslot][col + 1] == 'o':
            if capacity1 + capacity2 >= party_size:
                available_combinations.append((table1_info, table2_info))

    return available_combinations

def generate_user_message(free_tables, combined_tables, party_size, timeslot):
    # Returns a message for the user
    if not free_tables and not combined_tables:
        return [f"Sorry, there are no tables available for a party of {party_size} at timeslot {timeslot}."]

    messages = []

    if free_tables:
        messages.append(f"Great news! The following tables are available at the time {timeslot}:")
        for table in free_tables:
            table_name, capacity = table.split('(')
            messages.append(f" - Table {table_name} (Seats {capacity.rstrip(')')})")

    if combined_tables:
        messages.append("\nAlternatively, we can combine tables to fit your group:")
        for table1, table2 in combined_tables:
            capacity1, capacity2 = int(table1.split('(')[1].rstrip(')')), int(table2.split('(')[1].rstrip(')'))
            messages.append(f" - Tables {table1.split('(')[0]} and {table2.split('(')[0]} together can seat {capacity1 + capacity2} people.")

    return messages


# Example usage
timeslot = 2
party_size = 4

free_tables = list_free_tables(restaurant_tables, timeslot)
single_table = find_table_for_party(restaurant_tables, timeslot, party_size)
all_available_tables = find_all_tables_for_party(restaurant_tables, timeslot, party_size)
combined_tables = find_combined_tables_for_party(restaurant_tables, timeslot, party_size)

# User message
messages = generate_user_message(all_available_tables, combined_tables, party_size, timeslot)

print("\n".join(messages))















# def get_free_tables(tables):
#     """
#     Level 1
#     Returns a list of table IDs (or entire objects) that are currently free.
#     """
#     free_tables = []
#     for table in tables:
#         if not table["occupied"]:  # occupied == False
#             free_tables.append(table["table_id"])
#     return free_tables


# def find_one_table_for_size(tables, party_size):
#     """
#     Level 2
#     Returns the first table ID that can seat 'party_size' and is free,
#     or None if none found.
#     """
#     for table in tables:
#         if not table["occupied"] and table["capacity"] >= party_size:
#             return table["table_id"]
#     return None


# def find_all_tables_for_size(tables, party_size):
#     """
#     Level 3
#     Returns a list of all table IDs that can seat 'party_size' and are free.
#     """
#     suitable_tables = []
#     for table in tables:
#         if not table["occupied"] and table["capacity"] >= party_size:
#             suitable_tables.append(table["table_id"])
#     return suitable_tables


# def find_tables_including_combos(tables, party_size):
#     """
#     Level 4
#     Returns a list of table or table combinations that can seat 'party_size'.
#     Adjacent combos are determined via the table's "neighbors" list.
    
#     Example output structure:
#     [(1,), (3,), (1,2), (3,5)]  # Each tuple is a single table or a pair.
#     """
#     results = []

#     for table in tables:
#         # Check single table
#         if (not table["occupied"]) and (table["capacity"] >= party_size):
#             results.append((table["table_id"],))
        
#         # Check neighbor combos if single table can't seat them
#         if table["neighbors"] and not table["occupied"]:
#             for neighbor_id in table["neighbors"]:
#                 neighbor_table = next((t for t in tables if t["table_id"] == neighbor_id), None)
                
#                 # If neighbor also exists, is free, and combined capacity meets needs
#                 if neighbor_table and (not neighbor_table["occupied"]):
#                     total_capacity = table["capacity"] + neighbor_table["capacity"]
#                     if total_capacity >= party_size:
#                         # Sort to avoid duplicates like (1,2) and (2,1)
#                         combo = tuple(sorted([table["table_id"], neighbor_table["table_id"]]))
#                         if combo not in results:
#                             results.append(combo)
    
#     return results


# def friendly_output(tables, combos):
#     """
#     Bonus:
#     Takes the combos from Level 4 (like [(1,), (2,), (1,2)]) and
#     prints a more user-friendly message about each result.
#     """
#     for group in combos:
#         if len(group) == 1:
#             # Single table
#             table_id = group[0]
#             tdata = next((t for t in tables if t["table_id"] == table_id), None)
#             if tdata:
#                 print(f"Table {table_id} is free and can seat {tdata['capacity']} people.")
#         else:
#             # Combined tables
#             t1_id, t2_id = group
#             t1_data = next((t for t in tables if t["table_id"] == t1_id), None)
#             t2_data = next((t for t in tables if t["table_id"] == t2_id), None)
#             if t1_data and t2_data:
#                 total_capacity = t1_data["capacity"] + t2_data["capacity"]
#                 print(f"Tables {t1_id} and {t2_id} together can seat {total_capacity} people.")


# # -----------------------------------------------------------------------------
# # Example usage / testing:
# if __name__ == "__main__":
#     # Example data
#     tables_data = [
#         {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
#         {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
#         {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
#         {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
#     ]

#     print("LEVEL 1: Free Tables =", get_free_tables(tables_data))

#     print("LEVEL 2: One table for party size 2 =", find_one_table_for_size(tables_data, 2))

#     print("LEVEL 3: All tables for party size 2 =", find_all_tables_for_size(tables_data, 2))

#     combos = find_tables_including_combos(tables_data, 5)
#     print("LEVEL 4: Single or combined tables for party size 5 =", combos)

#     print("\nBONUS: Friendly output for the combos above")
#     friendly_output(tables_data, combos)
