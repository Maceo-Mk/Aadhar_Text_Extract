*****************************************************
OBJECTIVE:
*****************************************************
	The main objective of this project is to extract all details from Aadhar card and filter the required data.
		Information like - 
					Name, Year of Birth, UID


*****************************************************
SOLUTION:
*****************************************************
	Steps:
		-> Take image
		-> crop to box(which has text in it)
		-> convert into gray scale(mono crome)
		-> give to tesseract
		-> text(output of tesseract)
	Now we will process this text means we will get meaningful information from it.
		-> find name using name database
		-> find year of birth
		-> find for Aadhar ID(UID)
	for verfication please see aadhar_detail.txt file
	Steps followed for convert the image:

    Original Image:
    The following is a sample image containing some random data. 
   ![Aadhaar to JSON](original.jpg?raw=true "Aadhaar Card image")
    
    Grayscale Image:
    Since the colour of the image is not an important feature, it’s better to convert the image from three colour channels to one colour channel, preferably grayscale.
   ![Aadhaar to JSON](Gray_scale.png?raw=true "Aadhaar Card image")
*****************************************************
LIBRARIES USED:
*****************************************************
	•	pytesseract
    •	openCV
    •	pillow
    •	numpy



*****************************************************
Structure and Usage
*****************************************************
	Directories:
		src-
			which contains code files		

*****************************************************
:100:
