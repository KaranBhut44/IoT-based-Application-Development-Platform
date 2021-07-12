import os
import sys
from os import listdir
from os.path import isfile, join



def get_app_path():
    app_path = sys.argv[0]
    
    
    app_folder_path = app_path.rsplit('/',1)[0]
    return app_folder_path

def generate_docker_file():
    app_path = get_app_path()
    app_id = sys.argv[1]
    
    
    docker_file_path = app_path + '/' "Dockerfile" 
    print(docker_file_path)
    print(app_path)
    print("docker_file_path :", docker_file_path)
    with open(docker_file_path, "w") as f: 
        f.write("FROM python:3\n")
        f.write("COPY requirements.txt ./\n".format(app_path,app_path))
        f.write("RUN pip install --no-cache-dir -r requirements.txt\n".format(app_path))
        onlyfiles = [f for f in listdir(app_path) if isfile(join(app_path, f))]
        # print("File_name :",onlyfiles)
        add_files_str = "ADD" 
        for file_name in onlyfiles:
            if (file_name == "docker_file_generator.py" or file_name == "requirements.txt" or file_name == "Dockerfile" or file_name == "start.sh"):
                # print(file_name)
                continue
            add_files_str += " {}".format(file_name)

	#onlydir = [f for f in listdir(app_path) if not isfile(join(app_path, f))]
	#for file_name in onlydir:
	#    for f in os.listdir(file_name):
        #    	add_files_str += " {}/{}".format(file_name, f)

        add_files_str += ' ./'
        print(add_files_str)
        f.write(add_files_str+ '\n')
        
        f.write("ADD templates ./templates \n")
        f.write("ADD configuration ./configuration \n")
        f.write("ADD repository ./repository \n")
        # f.write("ADD application_helper ./application_helper \n")
        
        f.write('CMD ["python", "-u","ui_appmanager.py"]')



if __name__ == "__main__":
    generate_docker_file()


