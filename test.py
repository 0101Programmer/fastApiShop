# objects_per_page = 5
# sub_objects_box = []
# total_objects = [_ for _ in range(14)]
# main_objects_box = []
#
# inserted_obj_counter = 0
# for obj in total_objects:
#
#     sub_objects_box.append(obj)
#     inserted_obj_counter += 1
#
#     if len(sub_objects_box) < objects_per_page and (inserted_obj_counter + objects_per_page) < (len(total_objects)):
#         continue
#
#     elif len(sub_objects_box) == objects_per_page:
#         print(inserted_obj_counter)
#         sub_objects_box_copy = sub_objects_box.copy()
#         main_objects_box.append(sub_objects_box_copy)
#         sub_objects_box.clear()
#
#     elif len(sub_objects_box) < objects_per_page and (inserted_obj_counter + objects_per_page) > (len(total_objects)):
#         if sub_objects_box[-1] != total_objects[-1]:
#             continue
#         main_objects_box.append(sub_objects_box)
#
# print(main_objects_box)

def nested_lists_maker(all_objects: list, nested_list_len: int):
    nested_list = []
    main_list = []
    inserted_objects_counter = 0

    for object in all_objects:
        nested_list.append(object)
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


test_list = ['a', 'b', 'c', 'd', 'f', 'g', 'e', 'c', 'j', 'k', 'l', 'p', '111', ]

print(nested_lists_maker(test_list, 5))