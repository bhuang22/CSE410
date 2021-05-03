from cv2 import cv2
import fingerprint_feature_extractor
import os
import fingerprint_enhancer								


if __name__ == '__main__':
    img = cv2.imread('enhance_finger.jpg', 0)	
    #enhance= fingerprint_enhancer.enhance_Fingerprint(img)
    #cv2.imshow('enhance',enhance)
    #canny = cv2.Canny(img,125,175)
    #eroded = cv2.erode(canny,(3,3),iterations=1)
    # #cv2.imshow('canny edge',canny)
    # #cv2.imshow('erode edge',eroded)
    #cv2.imwrite('enhance_finger.jpg', enhance)

    #cv2.imwrite('2.jpg', enhance)
    # img2 = cv2.imread('2.jpg', 0)	
    # img = cv2.imread('2.jpg', 0)	

    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, showResult=True,spuriousMinutiaeThresh=10)
    cv2.waitKey(0)