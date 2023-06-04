
import shutil

def save_file(save_name):
    # Specify the paths and names of the original file and the copy
    original_file = file_name
    destination_directory = Path            #"C:\Users\Snehasish\Documents\Quiz_game\questions"
    copy_file = save_name+".txt"

    # Construct the full path of the copy file in the destination directory
    copy_file_path = f"{destination_directory}/{copy_file}"

    # Copy the contents of the original file to the copy file in the destination directory
    shutil.copyfile(original_file, copy_file_path)

'''*************************************[FUNCTIONS]**********************************************'''

# print('Instructions:\nI.create an empty .txt file & pass the path directory to Path And file-NAME to file_name')
file_name = 'files_txt.txt'
# File path to save files
Path = r"C:\Users\Snehasish\Documents\Quiz_game\questions"

def save_as_file(Q , n):
    append_Q = open(file_name , 'a')
    append_Q.write(f'{Q}\n')
    append_Q.close()

    # s_file_name = input('file name:  ').lower()     # file name  -input
    # s_file_as = input('file type:  ').lower()       # file type  -input
    save_file(n)                         # Above two attributes will be passed to this function
    wipe_all = open(file_name, 'w')  # After saving the file , parent-> file gets wiped out.
    wipe_all.truncate(0)
    wipe_all.close()
        
