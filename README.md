## Rwanda

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)


This is Frappe Application that returns provinces, districts, sectors, villages and cells found in Rwanda.

Rwanda is organized by: 
- 5 provinces
- 30 Districts
- 416 Sectors 
- 2148 Cells and 
- 14837 Villages.

## Table of Content
- [Rwanda](#rwanda)
- [Table of Content](#table-of-content)
- [Install](#install)
- [Usage](#usage)
- [Functions](#functions)
  - [`get_provinces()`](#get_provinces)
  - [`get_districts(province=None)`](#get_districtsprovincenone)
  - [`get_sectors(province=None, district=None)`](#get_sectorsprovincenone-districtnone)
    - [Example 1: Retrieve all sectors](#example-1-retrieve-all-sectors)
    - [Example 2: Retrieve sectors in a specific province](#example-2-retrieve-sectors-in-a-specific-province)
    - [Example 3: Retrieve sectors in a specific  district](#example-3-retrieve-sectors-in-a-specific--district)
    - [Example 3: Retrieve sectors in a specific province and district](#example-3-retrieve-sectors-in-a-specific-province-and-district)
  - [`get_cells(province=None, district=None, sector=None)`](#get_cellsprovincenone-districtnone-sectornone)
    - [Example 1: Retrieve all cells](#example-1-retrieve-all-cells)
    - [Example 2: Retrieve cells in a specific province](#example-2-retrieve-cells-in-a-specific-province)
    - [Example 3: Retrieve cells in a specific province and district](#example-3-retrieve-cells-in-a-specific-province-and-district)
    - [Example 4: Retrieve cells in a specific province, district, and sector](#example-4-retrieve-cells-in-a-specific-province-district-and-sector)
  - [`get_villages(province="OL05000025", district="OL04000150", sector="OL03002010", cell="OL02010410")`](#get_villagesprovinceol05000025-districtol04000150-sectorol03002010-cellol02010410)
    - [Example 1: Retrieve all cells](#example-1-retrieve-all-cells-1)
    - [Example 2: Retrieve cells in a specific province](#example-2-retrieve-cells-in-a-specific-province-1)
    - [Example 3: Retrieve cells in a specific province and district](#example-3-retrieve-cells-in-a-specific-province-and-district-1)
    - [Example 4: Retrieve cells in a specific province, district, and sector](#example-4-retrieve-cells-in-a-specific-province-district-and-sector-1)
  - [`search_region(region_name, region_types=None)`](#search_regionregion_name-region_typesnone)
    - [License](#license)


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

### `search_region(region_name, region_types=None)`
Search for regions by name (case-insensitive) in the specified region types or all region types. Returns a list of matching results.

```python
search_results = search_region(region_name="Kigali", region_types=["Province", "Villages"])
```


#### License

MIT