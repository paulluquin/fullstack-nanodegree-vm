Database Queries
This program allows the use of a python file "project.py" to run a webserver
	within vagrant, open project.py to start the webserver.
To open project.py, use vagrant to start the virtual machine (ie $vagrant up, $vagrant ssh). Once the virtual machine is running point to the "catalog" directory and run project.py ("$python project.py")
	
Use a web browser to go to localhost:5000 to access the web-interface

A copy of the database can be used (DealershipInventory), or it can be deleted and recreated using "DatabaseSetup.py"

This interface can be used to:
  -view all cars currently in the database
  -add a new cars
  -edit a current cars
  -delete a cars
  Each car has options linked to that car
    -Select the details of the car to see the optionSummary
    Options can be:
      -viewed
      -added
      -modified
      -removed

Requirements:
	- Virtual Box (Download link -> https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
	- vagrant (Download link -> https://www.vagrantup.com/downloads.html)
	- Virtual Machine (Download link -> https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
	- psql
	- SQL database (download link -> https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


This project was written with the Full Stack Nanodegree course as a baseline. The login and logout created during the course were used in this project.
