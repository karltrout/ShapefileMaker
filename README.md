<img src="icon.png" align="right" />

# README
## Convert ARTCC boundries to shapfile
- ## env setup
	- ### Checkout project
		```sh
		>cd ~
		>git clone git@github.com:karltrout/ShapefileMaker.git
		```
	- ### down load the latest ARTCC csv file from https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/center_surface_boundaries/

- ## run the script
  - ### change directory to ShapefileMaker
      ```sh
    >  source ./venv/bin/activate 
    >  python main.py -i path/to/downloaded/csv
      ```
