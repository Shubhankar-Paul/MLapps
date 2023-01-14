import torch, cv2, os 


def load_cardiac_model():
    
    weights = "allapps/detection/cardiac_detection/files/best.pt"
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=os.path.abspath(weights) ) 

    return model


def Cardiac(img,model):
    img_size = (224,224)

    image = cv2.resize(img, img_size, interpolation = cv2.INTER_LINEAR)
    
    results = model(image,size=img_size[0]) 

    for xmin,	ymin,	xmax,	ymax,	conf,	cls_idx in results.xyxy[0]:
            
        x1,y1,x2,y2 = int(xmin.item()),int(ymin.item()),int(xmax.item()),int(ymax.item())

        text = f'Pred:{conf.item():.1%}'

        cv2.rectangle(image,(x1,y1), (x2,y2), (0,255,0), 1)
        cv2.rectangle(image,(x1,y2+3),(x1+len(text)*10,y2+18), (0,255,0), -1)
        cv2.putText(image, text, (x1, y2+16), 0, 0.55, (0, 0, 0), 1)

        output_image = cv2.resize(image, (img.shape[1],img.shape[0]), interpolation = cv2.INTER_LINEAR)

        return output_image


