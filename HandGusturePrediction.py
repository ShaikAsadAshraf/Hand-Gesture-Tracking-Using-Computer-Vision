import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
mySerial = SerialObject("COM7", 9600)
while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False) # without draw
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        mySerial.sendData(fingers1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
