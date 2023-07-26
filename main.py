import os
import sys
from graphviz import Digraph

# Variables
DIRECTORY = ''
FORMAT = 'png'
STYLE = 'TB'
OUTPUT_FILE_NAME = 'Graph'
CUSTOM_FOLDER = ''
CUSTOM_FILE = ''
BG_COLOR = '#ffffff'
FOLDER_FONT_COLOR = '#171717'
FILE_FONT_COLOR = '#ffffff'
FONT_NAME = 'Arial'
FONT_SIZE = '12'

# Error messages for different scenarios
ERROR_DIR = "Please provide the folder directory using the '-dir' option to visualize the given folder structure."
ERROR_FORMAT = "Invalid output format! The '-f' option only supports 'png', 'svg', and 'PDF' formats for the graph. Please use one of these formats."
ERROR_STYLE = "Invalid graph style! The '-s' option supports 'TB', 'BT', 'RL', and 'LR' styles. Please choose a valid style."
ERROR_OUTPUT_FILE_NAME = "Invalid file name! Please provide a valid file name without special characters using the '-ot' option for the graph."
ERROR_CUSTOM_FOLDER = "Invalid format! Please provide the custom folder icon in 'png' format with the exttension '.png' using the '-cfr' option."
ERROR_CUSTOM_FILE = "Invalid format! Please provide the custom file icon in 'png' format with the exttension '.png' using the '-cfl' option."
ERROR_BG_COLOR = "Invalid background color! Please provide a valid background color code with '#' using the '-bgc' option."
ERROR_FOLDER_FONT_COLOR = "Invalid font color! Please provide a valid font color code with '#' using the '-flfc' option."
ERROR_FILE_FONT_COLOR = "Invalid font color! Please provide a valid font color code with '#' using the '-fifc' option."
ERROR_FONT_NAME = "Invalid font name! Please provide a valid font name using the '-fn' option."
ERROR_FONT_SIZE = "Invalid font size! Please provide a valid font size using the '-fs' option."
INDEX_ERROR = "Missing value for the argument."

# Class to handle folder structure visualization
class StructureVisualizer():
    def main(self):
        global DIRECTORY, FORMAT, STYLE, OUTPUT_FILE_NAME, CUSTOM_FOLDER, CUSTOM_FILE, BG_COLOR, FOLDER_FONT_COLOR, FILE_FONT_COLOR, FONT_NAME, FONT_SIZE

        # Display help and usage information if -h or --h is provided in the command line arguments
        if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''[=====[Help and Usage]=====]

Options:
  -dir   : Specify the folder directory to visualize its structure.
  -f     : Output format for the graph ('png', 'svg', or 'PDF'). Default is "png".
  -s     : Graph style (TB, BT, RL, or LR). Default is "TB".
           + TB: Top to bottom
           + BT: Bottom to top
           + RL: Right to left
           + LR: Left to right.

  -ot    : Specify the output file name for the graph.

Fonts:
  -fn    : Set the font name for the graph. Default is "Arial"
  -fs    : Customize folder and file name font size. Default is '12'
  
Colors:
  -bgc   : Background color for the graph. Default is "#ffffff"
  -flfc  : Font color for the folder name. Default is "#171717"
  -fifc  : Font color for the file name. Default is "#ffffff"

Custom Folder & File:
  -cfr   : Set a custom folder icon using a 'png' image (e.g-> folder.png)
  -cfl   : Set a custom file icon using a 'png' image (e.g-> file.png)''')

            
            exit()

        # Check if the -dir option is provided and set the DIRECTORY variable accordingly
        else:
            if '-dir' not in sys.argv:
                print(ERROR_DIR)
                exit()
            else:
                try:
                    DIRECTORY_Index = sys.argv.index('-dir') + 1
                    DIRECTORY = sys.argv[DIRECTORY_Index]
                    DIRECTORY = os.path.abspath(DIRECTORY)
                    DIRECTORY = rf"{DIRECTORY}"
                    if not os.path.exists(DIRECTORY):
                        print(ERROR_DIR)
                        sys.exit()

                    # Check and set other options if provided in the command line arguments
                    if '-f' in sys.argv:
                        try:
                            FORMAT_Index = sys.argv.index('-f') + 1
                            FORMAT = sys.argv[FORMAT_Index].lower()
                            if FORMAT not in ('png', 'svg', 'pdf'):
                                print(ERROR_FORMAT)
                                exit()
                            elif FORMAT == 'png':
                                print("Use 'svg' or 'pdf' format for better visualization.")
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()

                    if '-s' in sys.argv:
                        try:
                            STYLE_Index = sys.argv.index('-s') + 1
                            STYLE = sys.argv[STYLE_Index]
                            if STYLE not in ('TB', 'BT', 'RL', 'LR'):
                                print(ERROR_STYLE)
                                exit()
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()

                    if '-ot' in sys.argv:
                        try:
                            OUTPUT_FILE_NAME_Index = sys.argv.index('-ot') + 1
                            OUTPUT_FILE_NAME = sys.argv[OUTPUT_FILE_NAME_Index]
                            for char in OUTPUT_FILE_NAME:
                                if char in r'/\:*?"<>|':
                                    print(ERROR_OUTPUT_FILE_NAME)
                                    exit()
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()

                    if '-cfr' in sys.argv:
                        try:
                            CUSTOM_FOLDER_Index = sys.argv.index('-cfr') + 1
                            CUSTOM_FOLDER = sys.argv[CUSTOM_FOLDER_Index]
                            CUSTOM_FOLDER_PATH = os.path.abspath(CUSTOM_FOLDER)
                            CUSTOM_FOLDER_NAME = os.path.basename(CUSTOM_FOLDER_PATH)
                            extension = os.path.splitext(CUSTOM_FOLDER_NAME)[1]
                            if extension != '.png':
                                print(ERROR_CUSTOM_FOLDER)
                                exit()
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()

                    if '-cfl' in sys.argv:
                        try:
                            CUSTOM_FILE_Index = sys.argv.index('-cfl') + 1
                            CUSTOM_FILE = sys.argv[CUSTOM_FILE_Index]
                            CUSTOM_FILE_PATH = os.path.abspath(CUSTOM_FILE)
                            CUSTOM_FILE_NAME = os.path.basename(CUSTOM_FILE_PATH)
                            extension = os.path.splitext(CUSTOM_FILE_NAME)[1]
                            if extension != '.png':
                                print(ERROR_CUSTOM_FILE)
                                exit()
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                            
                    if '-bgc' in sys.argv:
                        try:
                            BG_COLOR_Index = sys.argv.index('-bgc') + 1
                            BG_COLOR = sys.argv[BG_COLOR_Index]
                            if BG_COLOR != 'transparent':
                                if BG_COLOR[0]!= '#':
                                    print(ERROR_BG_COLOR)
                                    exit()
                            BG_COLOR = str(BG_COLOR)
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                            
                    if '-flfc' in sys.argv:
                        try:
                            FOLDER_FONT_COLOR_Index = sys.argv.index('-flfc') + 1
                            FOLDER_FONT_COLOR = sys.argv[FOLDER_FONT_COLOR_Index]
                            if FOLDER_FONT_COLOR[0] != '#':
                                print(ERROR_FOLDER_FONT_COLOR)
                                exit()
                            FOLDER_FONT_COLOR = str(FOLDER_FONT_COLOR)
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                    
                    if '-fifc' in sys.argv:
                        try:
                            FILE_FONT_COLOR_Index = sys.argv.index('-fifc') + 1
                            FILE_FONT_COLOR = sys.argv[FILE_FONT_COLOR_Index]
                            if FILE_FONT_COLOR[0]!= '#':
                                print(ERROR_FILE_FONT_COLOR)
                                exit()
                            FILE_FONT_COLOR = str(FILE_FONT_COLOR)
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                    
                    if '-fn' in sys.argv:
                        try:
                            FONT_NAME_Index = sys.argv.index('-fn') + 1
                            FONT_NAME = sys.argv[FONT_NAME_Index]
                            
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                            
                    if '-fs' in sys.argv:
                        try:
                            FONT_SIZE_Index = sys.argv.index('-fs') + 1
                            FONT_SIZE = sys.argv[FONT_SIZE_Index]
                            if not FONT_SIZE.isdigit():
                                print(ERROR_FONT_SIZE)
                                exit()
                            FONT_SIZE = str(FONT_SIZE)
                        except IndexError:
                            print(INDEX_ERROR)
                            exit()
                except IndexError:
                    print(IndexError)
                    exit()

        # Start the visualization process
        self.visualize(DIRECTORY, FORMAT, STYLE, OUTPUT_FILE_NAME, CUSTOM_FOLDER, CUSTOM_FILE, BG_COLOR, FOLDER_FONT_COLOR, FILE_FONT_COLOR, FONT_NAME, FONT_SIZE)

    def visualize(self, _dir, _format, _style, _outputfile, _custom_folder, _custom_file, _background_color, _folder_font_color, _file_font_color, _font_name ,_font_size):
        def shorten_name(name, folder):
            # Shorten the name if it exceeds a certain length
            if len(name) > 10:
                if folder:
                    return name[:10] + "..."
                else:
                    extension = os.path.splitext(name)[1]
                    if len(extension) > 4:
                        return name[:3] + extension
                    else:
                        return name[:5] + ".." + extension
            return name

        # Initialize a Digraph object for graph visualization
        graphID = Digraph(format=_format, node_attr={'fontname': _font_name, 'fontsize':_font_size}, edge_attr={'fontname': _font_name, 'fontsize': _font_size}, graph_attr={'rankdir': _style, 'bgcolor': _background_color})
        parentFolder = os.path.basename(_dir)
        parentFolder = shorten_name(parentFolder, True)
        folder_count = 0
        file_count = 0

        # Add the root folder node to the graph
        if _custom_folder != '':
            graphID.node(parentFolder, labelloc='', shape='none', image=_custom_folder, fontcolor=_folder_font_color)
        else:
            graphID.node(parentFolder, labelloc='', shape='box', color='yellow', style='filled', fontcolor=_folder_font_color)

        # Traverse through the folder structure and add nodes for folders and files
        for root, folders, files in os.walk(_dir):
            for folder in folders:
                # Shorten the folder name and count the number of folders
                folder = shorten_name(folder, True)
                folder_count += 1

                # Add nodes for folders and connect them to their parent folders
                if _custom_folder != '':
                    graphID.node(folder, labelloc='', shape='none', image=_custom_folder, fontcolor=_folder_font_color)
                else:
                    graphID.node(folder, labelloc='', shape='box', color='yellow', style='filled', fontcolor=_folder_font_color)

                parent_folder = os.path.basename(root)
                graphID.edge(parent_folder, folder)

            for file in files:
                # Shorten the file name and count the number of files
                file = shorten_name(file, False)
                file_count += 1

                # Add nodes for files and connect them to their parent folders
                if _custom_file != '':
                    graphID.node(file, labelloc='', shape='none', image=_custom_file, fontcolor=_file_font_color)
                else:
                    graphID.node(file, labelloc='', shape='box', color='green', style='filled', fontcolor=_file_font_color)

                parent_folder = os.path.basename(root)
                graphID.edge(parent_folder, file)

        # Render the graph
        graphID.render(filename=_outputfile, view=True)
        print(f"Number of folders: {folder_count}\nNumber of files: {file_count}")

if __name__ == "__main__":
    visualizer = StructureVisualizer()
    visualizer.main()
    