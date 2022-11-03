import os

def sort_episodes():
    # get directory
    dir = os.getcwd() + '\\'

    # get list of files .mkv, .srt
    files = [file for file in os.listdir(dir) if file.endswith(('.mkv', '.avi', '.srt'))]

    # get nuber of episodes
    number_of_episodes = sum(1 for file in files if file.endswith(('.mkv')))

    for i in range(1, number_of_episodes + 1):
        # check folder exist and if not create new folder
        new_folder_path = dir + str(i) + '\\'
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        
        # episode title specification
        episode = "e0" + str(i) if i < 10 else "e" + str(i)
        for file in files:
            # add episode in specific for it
            if episode in file.lower():
                file_path = new_folder_path + file
                os.replace(file, file_path)

sort_episodes()