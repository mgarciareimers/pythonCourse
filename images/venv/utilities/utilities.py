import sys
import os
from PIL import Image


def transform_jpg_to_png(input_folder_path, output_folder_path):
    print('* JPG to PNG Image Converter *')
    print('  Starting conversion...')

    if not os.path.exists(input_folder_path):
        print('  Error => Starting folder does not exist, sorry.')
        return

    # Create output folder.
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    # Count jpg files.
    total_jpg = len([filename for filename in os.listdir(input_folder_path) if '.jpg' in os.path.splitext(filename)[1]])
    print(f'  Total jpg files to convert: { total_jpg }')

    # Get total size to convert.
    total_size = sum(os.path.getsize(f'{ input_folder_path }/{ filename }') for filename in os.listdir(input_folder_path) if '.jpg' in os.path.splitext(filename)[1])
    print(f'  Total size to convert: { round(total_size / 1e+6, 2) } MB')

    counter = 0
    converted_size = 0

    sys.stdout.write(f'\n\r  Progress: 0 %, 0  MB')

    for filename in os.listdir(input_folder_path):
        filename_split = os.path.splitext(filename)
        if '.jpg' in filename_split[1]:
            counter = counter + 1
            image = Image.open(f'{ input_folder_path }/{ filename }')
            converted_size = converted_size + os.path.getsize(image.filename)

            image.save(f'{ output_folder_path }/{ filename_split[0] }.png', 'png')

            sys.stdout.write(f'\r  Progress: { counter / total_jpg * 100 } %, { round(converted_size / 1e+6, 2) } MB')
            sys.stdout.flush()

    print('\n\n  Images have been successfully converted!')
