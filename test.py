def nested_lists_maker(all_objects: list, nested_list_len: int):
    nested_list = []
    main_list = []
    inserted_objects_counter = 0
    try:

        for obj in all_objects:
            nested_list.append(obj)
            inserted_objects_counter += 1

            if len(nested_list) < nested_list_len and (inserted_objects_counter + nested_list_len) < (len(all_objects)):
                continue

            elif len(nested_list) == nested_list_len:
                nested_list_copy = nested_list.copy()
                main_list.append(nested_list_copy)
                nested_list.clear()

            elif len(nested_list) < nested_list_len and (inserted_objects_counter + nested_list_len) > (len(all_objects)):
                if nested_list[-1] != all_objects[-1]:
                    continue
                main_list.append(nested_list)
                return main_list
    finally:
        return main_list


test_list = [i for i in range(100)]
print(nested_lists_maker(test_list, 2))
