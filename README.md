## Rwanda

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)


This is Frappe Application that returns provinces, districts, sectors, villages and cells found in Rwanda.

Rwanda is organized in four provinces in addition to the Kigali city, 30 Districts, 416 Sectors, 2148 Cells and 14837 Villages.


## Install

```cli
bench get-app  https://github.com/victor-abz/rwanda.git
bench --site site-name install-app rwanda
```

## Usage

```py
import province from rwanda
```

All inputs are case-insensitive.

### Provinces()

Returns array of country provinces.

```py
['East', 'Kigali', 'North', 'South', 'West']
```

### Districts()

By default it returns an array of country districts, if no params (province) is given

- Districts(province)

  If province is given it returns an array of districts found in that province.
  It returns `undefined` if province is not found.

### Sectors()

By default it returns array of country sectors, if no params (province, district) are given

- Sectors(province, district)

  If province and district are given it returns an array of sectors found from the given district in that province.
  It returns `undefined` if either province or district is not found.

### Cells()

By default it returns an array of all country cells.

- Cells(province, district, sector)

  if province, district and sector are given it returns an array of Cells found from the given sector.
  It returns `undefined` if either province, district or sector is not found.

### Villages()

By default it returns an array of all country villages.

- Villages(province, district, sector, cell)

  if province, district, sector and cell are given it returns an array of Villages found from the given cell.
  It returns `undefined` if either province, district , sector or cell is not found.


## License

MIT

#### License

MIT