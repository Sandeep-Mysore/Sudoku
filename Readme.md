Sudoku Solver 

Domain: Image Processing

Technologies & Concepts: Python, OpenCV2, MongoDB, Flask, Bootstrap3, jQuery

The project is a Sudoku solver implementing Image processing. The project accepts an image of the sudoku puzzle as input and display the solved sudoku puzzle as the output. The webcam is used to capture the image of the puzzle as input.
A front-end page built with bootstrap and jQuery displays the captured input image and displays the output image which is the solved solution to the puzzle.
A module named Scanner has been implemented. The purpose of this module is to read the captured image, optimize the image by pre-processing and transforms the image based on Contours.
The Scanner also recognizes the digits using OCR (Optical Character Recognition).
A Solver module written in Python, solves the puzzle using Back propagation and the results are displayed on the browser.
