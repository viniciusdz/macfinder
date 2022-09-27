# MacFinder

MacFinder is a Python script for search vendor of mac address list.

## Usage Example

```bash
python macfinder.py -f mac.txt
python macfinder.py --file mac.txt
python macfinder.py -m 00:15:5D:0A:C6:00
python macfinder.py -mac 00:15:5D:0A:C6:00
```

## Result Example

```bash
MAC: 00:15:5D:0A:C6:00 - VENDOR: Microsoft Corporation
MAC: 00:15:5D:0A:C6:01 - VENDOR: Microsoft Corporation
MAC: 00:15:5D:0A:C6:22 - VENDOR: Microsoft Corporation
MAC: 00:15:5D:0A:C6:3C - VENDOR: Microsoft Corporation
MAC: 00:15:5D:0A:C6:3D - VENDOR: Microsoft Corporation
MAC: 00:1D:D8:D2:CF:F6 - VENDOR: Microsoft Corporation
MAC: 00:1E:E5:AE:03:38 - VENDOR: Cisco-Linksys, LLC
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
