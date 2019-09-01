# running-faster-processes
Tips and tricks on running and checking processes, HTTP endpoints, caching, et el.

## On Ubuntu, run using pip3
	pip3 install -r requirements.txt

## To install with conda
	conda env create -n optimize -f environment.yml

## To initialise Redis server using docker
	docker run -d -p 6379:6379 redis:alpine

## To initialise PostgreSQL server using docker
	docker run -d -p 5432:5432 postgres:10-alpine

## To install wrk on Ubuntu
	sudo apt-get install build-essential libssl-dev git -y
	git clone https://github.com/wg/wrk git wrk
	cd wrk
	make
	sudo cp wrk /usr/local/bin
To use wrk:
	$ wrk http://localhost:8080/check_ip/1.0.0.4
 
