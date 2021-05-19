import cv2# import opencv library
import numpy as np
import pickle

def sudo_main(str_param):
	print "hello"
	pkl_file = open('init_model.pkl', 'rb')
	model = pickle.load(pkl_file)
	filename = 'hand_model.sav'
	classifier=pickle.load(open(filename, 'rb'))

	def rectify(h):
		print "hello"
		h = h.reshape((4,2))
		hnew = np.zeros((4,2),dtype = np.float32)
		add = h.sum(1)
		hnew[0] = h[np.argmin(add)]
		hnew[2] = h[np.argmax(add)]
		diff = np.diff(h,axis = 1)
		hnew[1] = h[np.argmin(diff)]
		hnew[3] = h[np.argmax(diff)]
		return hnew
	#reading the image
	img=cv2.imread(str_param,0)#read the image as grayscale image
	print ":imread"
	blur = cv2.GaussianBlur(img,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	biggest = None
	max_area = 0
	for i in contours:
			area = cv2.contourArea(i)
			if area > 100:
					peri = cv2.arcLength(i,True)
					approx = cv2.approxPolyDP(i,0.02*peri,True)
					if area > max_area and len(approx)==4:
						biggest = approx
						max_area = area
	approx=rectify(biggest)

	h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
	retval = cv2.getPerspectiveTransform(approx,h)
	warp = cv2.warpPerspective(img,retval,(450,450))

	sudo = np.zeros((9,9),np.uint8)
	smooth = cv2.GaussianBlur(warp,(3,3),3)
	thresh = cv2.adaptiveThreshold(smooth,255,0,1,5,2)
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	erode = cv2.erode(thresh,kernel,iterations =1)
	dilate =cv2.dilate(erode,kernel,iterations =1)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if 80<area<800:
			(bx,by,bw,bh) = cv2.boundingRect(cnt)
			if (80<bw*bh<1200) and (8<bw<40) and (20<bh<45):
				roi = dilate[by:by+bh,bx:bx+bw]
				small_roi = cv2.resize(roi,(10,10))
				feature = small_roi.reshape((1,100)).astype(np.float32)
				integer= model.predict(feature)
				if integer==7:
					small_roi = cv2.resize(roi,(8,8))
					feature = small_roi.reshape((1,64)).astype(np.float32)
					n=classifier.predict(feature)
					if n==7 or n==1:
						integer=n
				gridy,gridx = (bx+bw/2)/50,(by+bh/2)/50	# gridx and gridy are indices of row and column in sudo
				sudo.itemset((gridx,gridy),integer)
	print "before return"
	return sudo.tolist()
