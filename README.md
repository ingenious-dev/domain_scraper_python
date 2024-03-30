# Domain Scraper Python

_Powered by_ [![N|Solid](https://ingenious.or.ke/static//img/ingenious%20logo%20-%20cropped.png)](https://ingenious.or.ke/)

[![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/ingenious-dev/domain_scraper_python)

Python scripts for quickly checking the availabilty of web domains.

## Usage
Enter the desired domains in the file `domains.txt`. Each domain should be in a newline     
Run the script. See `Running the script` below      
Check the file `results/domains.xls` for the report on the availabilty of the domains

## Development setup
To setup a dev environment for coding, clone the repository and then run `make dev-setup` to setup a virtual environment with the needed dependencies.

## Running the script
Now you can run the program either using:

```
poetry run python domain_[SERVICE_PROVIDER].py
```

Or by entering the virtualenv and then running the program.
```
poetry shell

python domain_[SERVICE_PROVIDER].py
```

SERVICE_PROVIDER can be `hostpinnacle`, `kenyawebexperts` or `truehost`

### GUI Selector
```
poetry run python domain_gui.py
```

### Hostpinnacle
```
poetry run python domain_hostpinnacle.py
```

### Kenya Web Experts
```
poetry run python domain_kenyawebexperts.py
```

### Truehost
```
poetry run python domain_truehost.py
```

Test Windows Environment
```sh
OS Version:                10.0.22000 N/A Build 22000
OS Build Type:             Multiprocessor Free
```

## Benchmarrk
A search for `test.com` & `example.com` was run for each of the providers and total time taken measured. Here are the benchmarks:

| SERVICE_PROVIDER | TIME (Seconds) |
| --- | --- |
| Hostpinnacle | 0.703125 |
| Kenya Web Experts | 0.140625  |
| Truehost | 3.609375  |

This is not indicative of performance of their their service offering. It is only specific to domain search.

## Technologies
### Third Party Libraries
| NAME | DESCRIPTION |
| --- | --- |
| Poetry | Dependency manager |
| requests | send HTTP/1.1 requests extremely easily  |
| beautifulsoup4 | pulling data out of HTML and XML files  |
| xlwt | create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files  |

### Standard Libraries
| NAME | DESCRIPTION |
| --- | --- |
| threading | Run tasks simultaneously |
| tkinter | create and manipulate GUI widgets  |
| time | time-related functions  |
| codecs | encoders and decoders  |
| webbrowser | displaying web-based documents  |
| string | Common string operations  |
| itertools | Functions creating iterators for efficient looping  |

## Authors
Joseph Suhudu [Github @josuhudu](https://githug.com/josuhudu)

## Tips
To determine with service provider is cheaper the general rule is to check
`Registration Fee + Renew Fee` whichever is less is the more affordable one.          
ALWAYS CHECK THE `Renew Fee`.

# Credits
[![N|Solid](https://www.hostpinnacle.co.ke/wp-content/uploads/2018/10/logo21.png)](https://hostpinnacle.co.ke/)         
[![N|Solid](https://kenyawebexperts.co.ke/templates/joomla33/images/logo.png)](https://kenyawebexperts.co.ke/)
[![N|Solid](https://truehost.co.ke/cloud/assets/img/logo.png)](https://truehost.co.ke/)

All trademarks that appear in the document have been used for identification
purposes only and belong to their respective companies. 