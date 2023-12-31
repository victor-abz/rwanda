## Rwanda

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)


This is Frappe Application that provide provinces, districts, sectors, villages and cells found in Rwanda.

Rwanda is organized by: 
- 5 provinces
- 30 Districts
- 416 Sectors 
- 2148 Cells and 
- 14837 Villages.

## Install

```cli
bench get-app  https://github.com/victor-abz/rwanda.git
bench --site site-name install-app rwanda
```

## Usage

```py
from rwanda import get_provinces, get_districts, get_sectors, get_cells, get_villages
```


## Functions

### `get_provinces()`

This function retrieves a list of provinces along with their respective codes.

```python
provinces = get_provinces()
```

Returns array of country provinces object.

```py
[{"province_code": "OL05000025", "province_name": "Iburasirazuba"}, {"province_code": "OL05000020", "province_name": "Amajyaruguru"}, {"province_code": "OL05000015", "province_name": "Iburengerazuba"}, {"province_code": "OL05000010", "province_name": "Amajyepfo"}, {"province_code": "OL05000005", "province_name": "Umujyi wa Kigali"}]
```


### `get_districts(province=None)`
Retrieve a list of districts within a specified province code, or all districts if no province is provided.
```python
districts = get_districts(province="OL05000025")
```

### `get_sectors(province=None, district=None)`
Retrieve a list of sectors within a specified province code or district code, or all sectors if no province or district is provided.

```python
sectors = get_sectors(district="OL04000150")
```
#### Example 1: Retrieve all sectors
```python
all_sectors = get_sectors()
print(all_sectors)
```

#### Example 2: Retrieve sectors in a specific province
```python
sectors_in_province = get_sectors(province="OL05000025")
print(sectors_in_province)
```

#### Example 3: Retrieve sectors in a specific  district
```python
sectors_in_district = get_sectors(district="OL04000150")
print(sectors_in_district)
```

#### Example 3: Retrieve sectors in a specific province and district
```python
sectors_in_district = get_sectors(province="OL05000025", district="OL04000150")
print(sectors_in_district)
```


### `get_cells(province=None, district=None, sector=None)`

Retrieve a list of cells within a specified province, district, and sector, or all cells if no province, district, or sector is provided.

```python
cells = get_cells(province="OL05000025", district="OL04000150", sector="OL03002010")
```

#### Example 1: Retrieve all cells
```python
all_cells = get_cells()
print(all_cells)
```

#### Example 2: Retrieve cells in a specific province
```python
cells_in_province = get_cells(province="OL05000025")
print(cells_in_province)
```
#### Example 3: Retrieve cells in a specific province and district
```python
cells_in_district = get_cells(province="OL05000025", district="OL04000150")
print(cells_in_district)
```
#### Example 4: Retrieve cells in a specific province, district, and sector
```python
cells_in_sector = get_cells(province="OL05000025", district="OL04000150", sector="OL03002010")
print(cells_in_sector)
```

### `get_villages(province="OL05000025", district="OL04000150", sector="OL03002010", cell="OL02010410")`
Retrieve a list of villages within a specified province, district, sector, and cell, or all villages if no province, district, sector, or cell is provided.

```python
villages = get_villages(province="OL05000025", district="OL04000150", sector="OL03002010", cell="OL02010410")
```
# Example 1: Retrieve all villages
```python
all_villages = get_villages()
print(all_villages)
```
#### Example 2: Retrieve villages in a specific province
```python
villages_in_province = get_villages(province="OL05000025")
print(villages_in_province)
```
#### Example 3: Retrieve villages in a specific province and district
```python
villages_in_district = get_villages(province="OL05000025", district="OL04000150")
print(villages_in_district)
```
#### Example 4: Retrieve villages in a specific province, district, and sector
```python
villages_in_sector = get_villages(province="OL05000025", district="OL04000150", sector="OL03002010")
print(villages_in_sector)
```
#### Example 5: Retrieve villages in a specific province, district, sector, and cell
```python
villages_in_cell = get_villages(province="OL05000025", district="OL04000150", sector="OL03002010", cell="OL02010410")
print(villages_in_cell)
```

### `search_region(region_name, region_types=None)`
Search for regions by name (case-insensitive) in the specified region types or all region types. Returns a list of matching results.

```python
search_results = search_region(region_name="Kigali", region_types=["Province", "Villages"])
```

#### Example 1: Search for a region by name in all region types
```python
search_results_all_types = search_region(region_name="Rwamagana")
print(search_results_all_types)
```
#### Example 2: Search for a region by name in specific region types
```python
search_results_specific_types = search_region(region_name="Rwamanaga", region_types=["Sector", "Cell"])
print(search_results_specific_types)
```
## License

MIT