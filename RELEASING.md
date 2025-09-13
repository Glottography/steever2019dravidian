# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_steever2019dravidian.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_steever2019dravidian.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_steever2019dravidian.py
cldfbench zenodo --communities glottography cldfbench_steever2019dravidian.py
cldfbench readme cldfbench_steever2019dravidian.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| brah1256 | 0.00 | True | 1 |
| koda1255 | 0.24 | False | 1 |
| kota1263 | 0.32 | False | 1 |
| kuii1252 | 2.05 | False | 1 |
| kuru1301 | 1.04 | False | 1 |
| mala1464 | 0.00 | True | 3 |
| nucl1305 | 0.00 | True | 1 |
| pott1240 | 0.53 | False | 1 |
| sava1244 | 1.67 | False | 1 |
| sout1549 | 3.44 | False | 2 |
| tami1289 | 0.00 | True | 2 |
| telu1262 | 0.00 | True | 1 |
| toda1252 | 0.37 | False | 1 |
| tulu1258 | 0.09 | False | 1 |
