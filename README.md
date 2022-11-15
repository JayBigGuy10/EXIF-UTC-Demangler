# EXIF-UTC-Demangler
quick and short python script, to fix images which were taken with the wrong time zone offset (but still the correct actual time, this can't fix a bunch of photos with completely wrong times (yet))

takes one argument, the desired utc timezone for your images.

reads the /photos folder located in the directory of the script

takes existing exif utc offset / time in each image file, and calculates / updates these time values

heres how you run it, in this case to adjust images to utc+13 (NZDST)

```
py main.py 13
```

Link to the reference article I used to understand how to interact with exif in python [Read and Edit Image Metadata with Python - Kenneth Leung](https://towardsdatascience.com/read-and-edit-image-metadata-with-python-f635398cd991#9cfd)
