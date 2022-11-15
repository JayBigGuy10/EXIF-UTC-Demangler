from exif import Image
import os
from os import listdir
from os.path import isfile, join
import datetime
import sys

mypath = os.getcwd() + "\photos"
print(f'Current Path {mypath}')

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

target_offset = 13

if len(sys.argv) == 2:
    target_offset = sys.argv[1]

print(f'Adjusting to UTC offset of {target_offset}:00')


for img_path in onlyfiles:

    print(f'Current Photo File {img_path}')

    with open(f'{mypath}/{img_path}', 'rb') as img_file:

        img = Image(img_file)

    orig_time_offset = f'{img.get("offset_time")}'
    time_offset = orig_time_offset.split(":")[0]
    if time_offset is not None:
        print(f'No encoded UTC offset in {img_path}')
        break
    hours_to_add = abs(int(time_offset)-int(target_offset))
    #img.get("datetime")
    photodate = datetime.datetime.strptime(img.get("datetime"),'%Y:%m:%d %H:%M:%S')
    photodate = photodate + datetime.timedelta(hours=hours_to_add)

    photodate_string = photodate.strftime('%Y:%m:%d %H:%M:%S')

    img.datetime = photodate_string
    img.datetime_digitized = photodate_string
    img.datetime_original = photodate_string

    img.offset_time = str(target_offset)+":00"
    img.offset_time_digitized = str(target_offset)+":00"
    img.offset_time_original = str(target_offset)+":00"

    with open(f'{mypath}/{img_path}', 'wb') as new_image_file:
        new_image_file.write(img.get_file())
    






#'offset_time', 'offset_time_digitized', 'offset_time_original'

 #'datetime', 'datetime_digitized', 'datetime_original'

#https://towardsdatascience.com/read-and-edit-image-metadata-with-python-f635398cd991#9cfd

#  ['_exif_ifd_pointer',
#   '_gps_ifd_pointer', 
#   '_interoperability_ifd_Pointer',
#    'acceleration',
#     'artist',
#      'color_space',
#       'components_configuration',
#        'compression',
#         'contrast',
#          'copyright',
#           'custom_rendered',
#            'datetime',
#             'datetime_digitized',
#              'datetime_original',
#               'digital_zoom_ratio',
#                'exif_version',
#                 'exposure_bias_value',
#                  'exposure_mode',
#                   'exposure_program',
#                    'exposure_time',
#                     'f_number',
#                      'file_source',
#                       'flash',
#                        'flashpix_version',
#                         'focal_length',
#                          'focal_length_in_35mm_film',
#                           'gain_control',
#                            'gps_img_direction',
#                             'gps_img_direction_ref',
#                              'gps_version_id',
#                               'image_description',
#                                'jpeg_interchange_format',
#                                 'jpeg_interchange_format_length',
#                                  'light_source',
#                                   'make',
#                                    'maker_note',
#                                     'max_aperture_value',
#                                      'metering_mode',
#                                       'model',
#                                        'offset_time',
#                                         'offset_time_digitized',
#                                          'offset_time_original',
#                                           'orientation',
#                                            'photographic_sensitivity',
#                                             'pixel_x_dimension',
#                                              'pixel_y_dimension',
#                                               'pressure',
#                                                'resolution_unit',
#                                                 'saturation',
#                                                  'scene_capture_type',
#                                                   'sensitivity_type',
#                                                    'sharpness',
#                                                     'software',
#                                                      'temperature',
#                                                       'user_comment',
#                                                        'water_depth',
#                                                         'white_balance',
#                                                          'x_resolution',
#                                                           'y_and_c_positioning',
#                                                            'y_resolution']

