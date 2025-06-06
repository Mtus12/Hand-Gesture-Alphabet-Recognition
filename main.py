import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    alphabet = ''


    # ve ban tay
    if result.multi_hand_landmarks:
        myHand = []
        count = 0
        for idx, hand in enumerate(result.multi_hand_landmarks):
            mp_drawing.draw_landmarks(img, hand, mp_hand.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                h, w, _ = img.shape
                myHand.append([int(lm.x * w), int(lm.y * h)]) #x=0, y=1
            if myHand[4][0] < myHand[2][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'A'
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'B'
            elif myHand[4][0] > myHand[5][0] and myHand[8][0] > myHand[5][0] and myHand[12][0] > myHand[9][0] and myHand[16][0] > myHand[13][0] and myHand[20][1] > myHand[18][1]:
                alphabet = 'C'
            elif myHand[4][0] > myHand[12][0] and myHand[8][0] > myHand[5][0] and myHand[12][0] > myHand[9][0] and myHand[16][0] > myHand[13][0] and myHand[20][1] < myHand[18][1]:
                alphabet = 'D'
            elif myHand[4][0] < myHand[11][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'E'
            elif myHand[4][0] > myHand[2][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'F'
            elif myHand[4][0] < myHand[10][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'I'
            elif myHand[4][0] > myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'K'
            elif myHand[4][0] > myHand[2][0] and myHand[4][0] > myHand[12][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'L'
            elif myHand[4][0] > myHand[11][0] and myHand[8][0] < myHand[6][0] and myHand[12][0] < myHand[9][0] and myHand[16][0] < myHand[13][0] and myHand[20][0] < myHand[17][0]:
                alphabet = 'P'
            elif myHand[4][0] > myHand[11][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'S'
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'V'
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'W'
            elif myHand[4][0] > myHand[10][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'Y'



    cv2.putText(img, str(alphabet), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    # hien thi
    cv2.imshow("Detect hand", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()

