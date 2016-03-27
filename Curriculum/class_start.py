import os,sys, urllib




project_list = [
"hello_world.py",
"types_practice.py",
"formatters_escapes.py",
"calculator.py",

"tuples_lists.py",
"dictionaries_functions.py",
"loops.py",
"right_triangle.py",

"classes.py",
"inheritance.py",
"crypto.py",
"adventure.py",

"file_readwrite.py",
"argv_prac.py",
"os_mapper.py",
"os_builder.py",

"pyPDF2_app.py",
"csv_maker.py",
"json_xml_prac.py"
"bc_json_puller",

"urllib_prac.py",
"requests_apis.py",
"web_scraper.py",
"redditbot.py",
]

root_file = "PyAcademy"

if root_file in os.listdir(os.curdir):
    print "Directory already exists...please delete."
    sys.exit(1)
else:
    pass

counter = 0
my_folders = list()

os.mkdir(root_file)
print "Welcome to the Python Academy!\n\nBeginning Writing..."
for names in range(1,9):
    print "Writing Folder: Week_%s" % names
    my_folders.append("Week_%s" % names)


for folder in my_folders:
    os.mkdir(os.path.join(root_file,folder))
    end_counter = counter + 3
    target_path = os.path.join(root_file,folder)
    
    for class_file in project_list[counter:end_counter]:
        my_file = open("{}".format(os.path.join(os.curdir,target_path,class_file)),"w")
        my_file.write("#FILE: {}".format(class_file))
        my_file.close()
        print "Writing File: %s" % class_file

    counter = end_counter


utilities = os.path.join(root_file,"Utilities")
os.mkdir(utilities)

print "Retrieving Class files from the internet"
try:
    print "Retrieving Curriculum"
    urllib.urlretrieve("https://github.com/kerstentw/PythonAcademy/raw/master/Curriculum/Curriculum_sesh2.pdf",os.path.join(utilities,"Curriculum.pdf"))
    
    print "Retrieving Python DocsFILE: May take up to 5 minutes"
    urllib.urlretrieve("https://github.com/kerstentw/PythonAcademy/raw/master/Curriculum/python-2.7.11-docs-pdf-letter.zip",os.path.join(utilities,"python-2.7.11-docs-pdf-letter.zip"))

    print "Retrieving pip Installer"
    urllib.urlretrieve("https://bootstrap.pypa.io/get-pip.py",os.path.join(utilities,"get-pip.py"))



    print "...Files Retrieved"

except:
    print "!!500:connection error!!  Files not retrieved"


print "Done Writing"
