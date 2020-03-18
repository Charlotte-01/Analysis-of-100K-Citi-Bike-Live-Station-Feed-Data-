Analyzing Millions of NYC Parking Violations

Part 1: Python Scripting

Support below commend line:

$ docker run -v $(pwd):/app -e APP_KEY= {APP_KEY} -t sta:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json

Result: results.json & resuls.json

Part2:

$ docker-compose up -d

to build pyth:

$ docker-compose build pyth

part3:

to run the result to kibana:

$ docker-compose run -e APP_KEY={APP_KEY} -v ${pwd}:/app pyth python main.py --page_size=1000 --num_pages=10 --output=results.json --push_es=True