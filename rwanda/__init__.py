# Copyright (c) 2023, Victor Abizeyimana and contributors
# License: MIT. See LICENSE
"""
Rwanda - This is Frappe based Application that provides 
provinces, districts, sectors, villages and cells found in Rwanda.

Rwanda is organized by: 
- 5 provinces
- 30 Districts
- 416 Sectors 
- 2148 Cells and 
- 14837 Villages.

"""
from frappe import get_all

__version__ = "0.0.1"


def get_provinces():
    """
    Retrieve a list of provinces with specified fields.

    :return: List of dictionaries containing province_code and province_name.
    """
    return get_all("Province", fields=["province_code", "province_name"])


def get_districts(province=None):
    """
    Retrieve a list of districts within a specified province with specified fields.

    :param province: The code of the province to filter districts. If None, retrieves all districts.
    :return: List of dictionaries containing district_code and district_name.
    """
    filters = {"province_code": province} if province else {}
    return get_all("District", filters=filters, fields=["district_code", "district_name"])


def get_sectors(province=None, district=None):
    """
    Retrieve a list of sectors within a specified province and district with specified fields.

    :param province: The code of the province to filter sectors.
    :param district: The code of the district to filter sectors.
    :return: List of dictionaries containing province_code, district_code, sector_code, and sector_name.
    """
    filters = {}
    if province:
        filters["province_code"] = province
    if district:
        filters["district_code"] = district
    return get_all("Sector", filters=filters, fields=["province_code", "district_code", "sector_code", "sector_name"])


def get_cells(province=None, district=None, sector=None):
    """
    Retrieve a list of cells within a specified province, district, and sector with specified fields.

    :param province: The code of the province to filter cells.
    :param district: The code of the district to filter cells.
    :param sector: The code of the sector to filter cells.
    :return: List of dictionaries containing province_code, district_code, sector_code, cell_code, and cell_name.
    """
    filters = {}
    if province:
        filters["province_code"] = province
    if district:
        filters["district_code"] = district
    if sector:
        filters["sector_code"] = sector
    return get_all("Cell", filters=filters, fields=["province_code", "district_code", "sector_code", "cell_code", "cell_name"])


def get_villages(province=None, district=None, sector=None, cell=None):
    """
    Retrieve a list of villages with their codes and names in the specified province, district, sector, and cell.

    :param province: Optional. If provided, filters villages by the specified province.
    :param district: Optional. If provided, filters villages by the specified district.
    :param sector: Optional. If provided, filters villages by the specified sector.
    :param cell: Optional. If provided, filters villages by the specified cell.
    :return: A list of dictionaries containing province, district, sector, cell, village codes, and village names.
    """
    filters = {}

    if province:
        filters["province_code"] = province
    if district:
        filters["district_code"] = district
    if sector:
        filters["sector_code"] = sector
    if cell:
        filters["cell_code"] = cell

    return get_all("Village", filters=filters, fields=["province_code", "district_code", "sector_code", "cell_code", "village_code", "village_name"])


def search_region(region_name, region_types=None):
    """
    Search for a region by name (case-insensitive) in the specified region_types or all region_types.

    :param region_name: The name to search for in regions.
    :param region_types: A list of region types to search within. Defaults to all region types if None.
    :return: A list of dictionaries containing the type and data of matching regions.
             Returns None if no matching regions are found.
    """

    # List of all available region types
    all_region_types = ["Province", "District", "Sector", "Cell", "Village"]

    # If region_types is not provided, search in all region types
    if region_types is None:
        region_types = all_region_types
    # If a single region type is provided, convert it to a list
    elif isinstance(region_types, str):
        region_types = [region_types]

    # List to store the search results
    results = []

    # Iterate through each specified region type
    for region_type in region_types:
        # Construct the field name for the region name in the current region type
        field_name = f"{region_type.lower()}_name"

        # Set up filters for case-insensitive partial matching
        filters = {
            field_name: ["like", f"%{region_name.lower()}%"]
        }

        # Retrieve regions matching the filters
        if regions := get_all(
            region_type,
            filters=filters,
            fields=[
                "*",  # Retrieve all fields
            ],
        ):
            # Extend the results list with dictionaries containing the type and data of matching regions
            results.extend({"type": region_type, "data": region} for region in regions)

    # Return the results list or None if no matching regions are found
    return results or None