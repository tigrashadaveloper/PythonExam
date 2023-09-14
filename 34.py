from volume import calculate_volume
from area import calculate_area
from perimeter import calculate_perimeter

length = 10
width = 20
height = 30

volume_result = calculate_volume(length, width, height)
area_result = calculate_area(length, width, height)
perimeter_result = calculate_perimeter(length, width, height)

print(f"Объем = {volume_result}")
print(f"Площадь = {area_result}")
print(f"Периметр = {perimeter_result}")
