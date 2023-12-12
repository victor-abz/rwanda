from frappe import get_all

__version__ = "0.0.1"


def get_provinces():
    return get_all("Province", fields=["province_code", "province_name"])


def get_districts(province=None):
    filters = {"province_code": province} if province else {}
    return get_all(
        "District", filters=filters, fields=["district_code", "district_name"]
    )


def get_sectors(province=None, district=None):
    filters = {}
    
    if province:
        filters["province_code"] = province
    if district:
        filters["district_code"] = district
    
    return get_all("Sector", filters=filters, fields=["province_code", "district_code", "sector_code", "sector_name"])


def get_cells(province=None, district=None, sector=None):
    filters = {}
    
    if province:
        filters["province_code"] = province
    if district:
        filters["district_code"] = district
    if sector:
        filters["sector_code"] = sector
    
    return get_all("Cell", filters=filters, fields=["province_code", "district_code", "sector_code", "cell_code", "cell_name"])


def get_villages(province=None, district=None, sector=None, cell=None):
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
    # Search for a region by name (case-insensitive) in the specified region_types or all region_types
    all_region_types = ["Province", "District", "Sector", "Cell", "Village"]

    if region_types is None:
        region_types = all_region_types
    elif isinstance(region_types, str):
        region_types = [region_types]

    results = []
    for region_type in region_types:
        field_name = f"{region_type.lower()}_name"
        filters = {
            field_name: ["like", f"%{region_name.lower()}%"]
        }

        if regions := get_all(
            region_type,
            filters=filters,
            fields=[
                "*",
            ],
        ):
            results.extend({"type": region_type, "data": region} for region in regions)

    return results or None
