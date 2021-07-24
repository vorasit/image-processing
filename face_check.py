import cv2,sys,numpy,os;file='haarcascade/haarcascade_frontalface_default.xml';img='image';images,labels,names,id=([],[],{},0);value=int(input("Enter check=1 , data=2 : "));
if value==1:
    for subdirs,dirs,files in os.walk(img):
        for subdir in dirs:
            names[id] = subdir;subjectpath = os.path.join(img, subdir)
            for filename in os.listdir(subjectpath):
                path=subjectpath+'/'+filename;label=id;
                images.append(cv2.imread(path,0));
                labels.append(int(label))
            id+=1
    width,height=(130,100);images,labels=[numpy.array(lis)for lis in [images,labels]];face_cascade=cv2.CascadeClassifier(file);cap=cv2.VideoCapture(0)
    while True:
        rat,im=cap.read();gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2);face=gray[y:y+h,x:x+w];face_resize=cv2.resize(face,(width,height));model=cv2.face.LBPHFaceRecognizer_create();model.train(images,labels);prediction=model.predict(face_resize);cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            if prediction[1]<100:
                cv2.putText(im,'%s-%.0f'%(names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
            else:
                cv2.putText(im,'Unknown',(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
        cv2.imshow("Face",im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
elif value==2:
    print("Enter name folder:");filedata=input();img='image';sub_data=filedata;path=os.path.join(img,sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    width,height=(130,100);face_cascade=cv2.CascadeClassifier(file);cap=cv2.VideoCapture(0);count=1
    while count<10: 
        ret,im=cap.read();gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY);faces=face_cascade.detectMultiScale(gray,1.3,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2);face=gray[y:y+h,x:x+w];face_resize=cv2.resize(face,(width,height));cv2.imwrite('%s/%s.png'%(path,count),face_resize)
        count+=1;cv2.imshow('Data',im)
        if cv2.waitKey(150) & 0xFF == ord('q'):
            break
else:
    print("CODE BY GOD_PARAMAE")


