<H1>Link Analysis</H1>

<H2>How to run</H2>
(This readme assumes python 3)
* Unzip the packaged file and cd into the root directory.
* You should see several files/folders, including a run_tasks.py, setup.py, and several module folders.
* Run the following command: "python setup.py install"
* You should now see an output_files directory and an input_files directory
* Within input_files there are two folders, carbon_footprint and focused_crawl. 
* Place the documents you wish to run against in their respective folders
* The structure of the documents should be input_files/<sub_folder>/<filename>/<filename>.html
* To run the program, from the root directory run "python run_tasks.py [dampen_factor] --pr_iterations [x]"
* Use of --pr_iterations is optional and PageRank will run to convergence if not specified
* An example standard run is: "python run_tasks.py .85"
* The program will begin to print out the number of items it has graphed and ranked to st_out
* At the completion of the program, a set of files with the stats and answers related to the project will be in output_files
* I've also included a copy of these files from my runs against my documents