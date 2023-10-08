<img src="icon.png" align="right" />

# README
## Convert ARTCC boundries to shapfile
- ## env setup
	- ### Checkout project
		```sh
		>cd ~
		>git clone https://github.com/karltrout/ShapefileMaker.git
		```
	- ### download the latest ARTCC csv file from https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/center_surface_boundaries/

  - ### install python and requirements
      ```shell
    >   sudo apt install python3
    >   sudo apt install python3.10-venv
      ```

- ## run the script
  - ### change directory to ShapefileMaker
      ```sh
    > python3 -m venv ./
    > source ./bin/activate 
    > python -m pip install -r requirements.txt
    > python main.py -i path/to/downloaded/csv
      ```
