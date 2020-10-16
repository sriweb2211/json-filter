import json 

f = open('export-2020-10-14.json')
jsonObject = json.load(f)

data_img_name = []
data_height = []
data_width = []
data_objs = []
data_objs_category_name = []
data_objs_bbox = []
data_objs_obj = []
data_objs_isDifficult = []
info = []
info_name = []
data = []


# exit()
linecount = 0
for row in jsonObject:
    print(row['image-name'])

    single = {}
    single['img_name'] = row['image-name']
    single['height'] = 1333
    single['width'] = 1000

    # objs = {}
    # objs['test1'] = 1
    # objs['test2'] = 3
    # objs['test3'] = 2
    # single['objs'] = objs
    

    obj_data = {}
    obj = []
    obj_cat = []
    obj_bbox = []
    for row_label in row['Label']['objects']:
        print(row_label['value'])

        category = {}
        if row_label['value'] == 'inside_box':
            category = 1
        else:
            category = 2
        
        polygon = []
        for row_polygon in row_label['polygon']:
            print(row_polygon['x'])
            print(row_polygon['y'])

            polygon.append(row_polygon['x'])
            polygon.append(row_polygon['y'])


        obj_value = {}
        obj_value = row_label['value']


        # cat = {}
        # cat['category_id'] = category

        # poly = {}
        # poly['bbox'] = polygon

        # val = {}
        # val['obj'] = obj_value

        obj_info = {}
        obj_info['category_id'] = category
        obj_info['bbox'] = polygon
        obj_info['obj'] = obj_value
        obj_info['isDifficult'] = 0
        
        # obj_data['category_id'] = cat
        # obj_data['bbox'] = poly
        # obj_data['obj'] = val

        # obj_data['category_id'] = category
        # obj_data['bbox'] = polygon
        # obj_data['obj'] = obj_value



        # obj_cat.append(category)
        # obj_bbox.append(polygon)
        
        # obj_data['category_id'] = obj_cat
        # obj_data['bbox'] = obj_bbox

        # obj.append(obj_data)
        obj.append(obj_info)

    single['objs'] = obj
    
    

    # Final data to store one by one
    data.append(single)
    
    linecount += 1
f.close()

with open('output.json', 'w') as f:
    json.dump(data, f)