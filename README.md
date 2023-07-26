# Directory-Visualizer

Directory Visualizer is a user-friendly tool to visualize and explore the structure of directories in a tree-like view. Easily understand and navigate your file system by creating graph using this tool.

<img width="640px" src="https://github.com/ZedUnknown/Directory-Visualizer/blob/main/Images/Graph-bg.png" alt="Image"/>

## Prerequisites

- Python 3.x

## Installation
1. Clone the repository or download the project files.
```bash
git clone https://github.com/ZedUnknown/directory-visualizer.git
cd directory-visualizer
```
2. Install the required Python module (graphviz)
```
pip install graphviz
```

## Usage
To visualize the folder structure, run the main.py script with the following command-line options:
```
python main.py -dir <folder_name> -f <output_format> -ot <output_file_name> -cfr <custom_folder_icon.png> -cfl <custom_file_icon.png> -s <graph_style>
```

### Options

```
-dir   : Specify the folder directory to visualize its structure.
-f     : Output format for the graph ('png', 'svg', or 'PDF'). Default is "png".
-s     : Graph style (TB, BT, RL, or LR). Default is "TB".
         + TB: Top to bottom
         + BT: Bottom to top
         + RL: Right to left
         + LR: Left to right.

-ot    : Specify the output file name for the graph.

[Fonts]
-fn    : Set the font name for the graph. Default is "Arial"
-fs    : Customize folder and file name font size. Default is '12'
  
[Colors]
-bgc   : Background color for the graph. Default is "#ffffff"
-flfc  : Font color for the folder name. Default is "#171717"
-fifc  : Font color for the file name. Default is "#ffffff"

[Custom Folder & File]
-cfr   : Set a custom folder icon using a 'png' image (e.g-> folder.png)
-cfl   : Set a custom file icon using a 'png' image (e.g-> file.png)
```

### Example
```
python main.py -dir Project -f png -s TB -ot FolderStructure -fn Quicksand -fs 10 -bgc #e0e0e0 -flfc #000000 -fifc #008cff -cfr folder_img.png -cfl file_img.png
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Feedback and Suggestions
Your feedback and suggestions are valuable to us! If you encounter any problems, have ideas for improvement, or would like to suggest additional options, please feel free to:

- Open an issue in this repository to report a problem or bug.
- Submit a pull request if you have a solution or enhancement to contribute.
- Reach out to us through the contact information provided in the repository.

We appreciate your feedback and look forward to hearing from you!
---

Explore the Directory Visualizer and gain insights into the organization of files and subdirectories across various folders like never before!
