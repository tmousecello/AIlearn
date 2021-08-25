#  -------------------------------------------------------------
#   Copyright (c) Cavedu.  All rights reserved.
#  -------------------------------------------------------------

import argparse
import json
import os

import numpy as np
from PIL import Image

import tflite_runtime.interpreter as tflite

import cv2

import time

# 我加的
distractedUp = 0 # 抬頭的分心指數
distractedDown = 0 # 低頭的分心指數


def get_prediction(image, interpreter, signature):
    # process image to be compatible with the model
    input_data = process_image(image, image_shape)

    # set the input to run
    interpreter.set_tensor(model_index, input_data)
    interpreter.invoke()

    # grab our desired outputs from the interpreter!
    # un-batch since we ran an image with batch size of 1, and convert to normal python types with tolist()
    outputs = {key: interpreter.get_tensor(value.get("index")).tolist()[0] for key, value in model_outputs.items()}

    # postprocessing! convert any byte strings to normal strings with .decode()
    for key, val in outputs.items():
        if isinstance(val, bytes):
            outputs[key] = val.decode()

    return outputs

# 即時影像縮放
def process_image(image, input_shape):
    width, height = image.size
    # ensure image type is compatible with model and convert if not
    input_width, input_height = input_shape[1:3]
    if image.width != input_width or image.height != input_height:
        image = image.resize((input_width, input_height))

    # make 0-1 float instead of 0-255 int (that PIL Image loads by default)
    image = np.asarray(image) / 255.0
    # format input as model expects
    return image.reshape(input_shape).astype(np.float32)

# 主程式 不建議動
def main():    
    global signature_inputs
    global input_details
    global model_inputs
    global signature_outputs
    global output_details
    global model_outputs
    global image_shape
    global model_index
    # --model參數設定流程
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model',
        help='Model path of saved_model.tflite and signature.json file',
        required=True)
    parser.add_argument('--video',
        help='Set video number of Webcam.',
        required=False, type=int, default=0)
    args = parser.parse_args()
    
    with open( args.model + "/signature.json", "r") as f:
        signature = json.load(f)

    model_file = signature.get("filename")

    interpreter = tflite.Interpreter(args.model + '/' + model_file)
    interpreter.allocate_tensors()
    # print('interpreter=',interpreter.get_input_details())

    # Combine the information about the inputs and outputs from the signature.json file with the Interpreter runtime
    signature_inputs = signature.get("inputs")
    input_details = {detail.get("name"): detail for detail in interpreter.get_input_details()}
    model_inputs = {key: {**sig, **input_details.get(sig.get("name"))} for key, sig in signature_inputs.items()}
    signature_outputs = signature.get("outputs")
    output_details = {detail.get("name"): detail for detail in interpreter.get_output_details()}
    model_outputs = {key: {**sig, **output_details.get(sig.get("name"))} for key, sig in signature_outputs.items()}
    image_shape = model_inputs.get("Image").get("shape")
    model_index = model_inputs.get("Image").get("index")

    cap = cv2.VideoCapture(args.video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    key_detect = 0
    times = 1
    

    # 無窮迴圈開始(要改的地方)
    while (key_detect == 0):
        ret,image_src = cap.read()

        frame_width = image_src.shape[1]
        frame_height = image_src.shape[0]

        cut_d = int((frame_width-frame_height)/2)
        crop_img = image_src[0:frame_height,cut_d:(cut_d+frame_height)]

        image = Image.fromarray(cv2.cvtColor(crop_img,cv2.COLOR_BGR2RGB))

        if (times==1):
            prediction = get_prediction(image, interpreter, signature)

            # print('Result = '+ prediction["Prediction"])
            # print(prediction)

            Label_name = signature['classes']['Label'][prediction['Confidences'].index(max(prediction['Confidences']))]
            print(Label_name)
            print('Confidences = ' + str(max(prediction['Confidences'])) )
        # 顯示字
        cv2.putText(crop_img, Label_name + " " +
            str(round(max(prediction['Confidences']),3)),
            (5,30), cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0,255,255), 6, cv2.LINE_AA)
        cv2.putText(crop_img, Label_name + " " +
            str(round(max(prediction['Confidences']),3)),
            (5,30), cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0,0,0), 2, cv2.LINE_AA)
        #  cv2.putText(crop_img即時影像, Label_name標籤名稱 + " " +後面就是信心分數
        #     str(round(max(prediction['Confidences']),小數點位數)),
        #     (5,30), cv2.FONT_HERSHEY_SIMPLEX, 1,
        #     (字的內裡顏色B,G,R), 粗細, cv2.LINE_AA)
            if distractedDown
        

        cv2.imshow('Detecting....',crop_img)

        times=times+1
        if (times >= 30): # 我的webcam的fps是30
            times=1

        read_key = cv2.waitKey(1)
        if ((read_key & 0xFF == ord('q')) or (read_key == 27) ):
            key_detect = 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
