# Urine Test Color Identifier 🧪
##### Due to time constraints I could not rewrite the application in Flask.

### Relevant Files
- [Color Extraction](/color_extract/extract_color.py)
- [Views](/color_extract/views.py)
- [Tests](/color_extract/tests.py)
- [Strip Model](/color_extract/models.py)
- [Strip Form](/color_extract/forms.py)
  
Code is commented.

**Tests have been written for Instance creation and functions**
*refer `color_extract/tests.py`*

### How to run
- Clone the repo
- `cd main`
- run `pip install -r requirements.txt`
- `python manage.py runserver`

### How to run Tests locally(There is a CI pipeline setup)
- Clone the repo
- `cd main`
- run `pip install -r requirements.txt`
- `python manage.py test color_extract`


### Web App
TechStack used:
- Django
- OpenCV
- Bootstrap

**How it works**
- user makes a POST request by uploading appropriate file
- **Note:** Only jpg,png,jpeg files are allowed. Otherwise user gets an error message asking them to do the same
- The uploaded file is passed through `color_extract` function
- returns color_value dict. This is saved as an object instance `StripFile` along with the image.
- renders the value dict on the same webpage


### Output
![sample1](./strip_images/sample1.png)

![sample-error](./strip_images/sample2.png)
