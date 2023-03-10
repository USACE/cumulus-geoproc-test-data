# Release Notes

## HRRR Total Precip

Forecast hour `00` does not have `01 hr Total precipitation [kg/(m^2)]` a band.  The test results in `0` as the band number.  Attributes to find a band that is not there should have the key set to `0`.  See the following example:

```
"attr": {
    "0": {
        "GRIB_COMMENT": "01 hr Total precipitation [kg/(m^2)]",
        "GRIB_ELEMENT": "APCP01",
        "GRIB_UNIT": "[kg/(m^2)]"
    },
    "25": {
        "GRIB_COMMENT": "Geopotential height [gpm]",
        "GRIB_SHORT_NAME": "85000-ISBL",
        "GRIB_ELEMENT": "HGT",
        "GRIB_UNIT": "[gpm]"
    }
}
```

## NBM CO 01h

Band numbers for Temperature and 01 hr QPF have changed.  Attribute keys have been updated to reflect this change.  The following attributes have been updated for both NBM test products:

```
"attr": {
    "273": {
        "GRIB_COMMENT": "Temperature [C]",
        "GRIB_ELEMENT": "T",
        "GRIB_SHORT_NAME": "2-HTGL",
        "GRIB_UNIT": "[C]"
    },
    "234": {
        "GRIB_ELEMENT": "QPF01",
        "GRIB_SHORT_NAME": "0-SFC"
    }
}
```