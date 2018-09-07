from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
import requests, json
from .serializers import *
from .models import *

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FaceCreate(generics.ListCreateAPIView):
    """This class defines the face create behavior of our rest api."""
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        """Save the post data when creating a new face."""
        print(serializer)
        serializer.save()

class FaceView(generics.ListAPIView):
    """This class handles the face http GET, PUT and DELETE requests."""
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Create your views here.
def index(request):
    return HttpResponse('test')


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



def demo(request):
    body = json.loads(request.body.decode('utf-8'))
    # with open("face.jpeg", "wb") as fh:
    #     fh.write(base64.b64decode(body['img_data']))
    # image = cv2.imread("face.jpeg")
    # image = imutils.resize(image, width=600)
    # cv2.imwrite('face.jpeg',image)
    #  # Create the haar cascade
    # faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    # eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    # # Read the image
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # Detect faces in the image
    # faces = faceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.5,
    #     minNeighbors=5,
    #     minSize=(20, 20),
    #     maxSize = (400, 400)
    # )


    # # print("Found {0} faces!".format(len(faces)), faces)

    # # # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #     print('FACE',x, "left",y, "top",x+w, "right",y+h,"bottom",w,h)
    #     fwid=w
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = image[y:y+h, x:x+w]
    #     eyes = eyeCascade.detectMultiScale(
    #         roi_gray,
    #         scaleFactor=1.01,
    #         minNeighbors=5,
    #         minSize=(48, 48),
    #         maxSize=(65, 65)
    #     )
    #     hairline = 0
    #     ebot = 0
    #     eyewid = []
    #     for (ex,ey,ew,eh) in eyes:
    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    #         print('EYE', "left", ex, "top", ey, "right", ex+ew,"bottom", ey+eh, "width", ew, "height", eh)
    #         hairline = hairline+ey+eh/2
    #         ebot = ebot + (ey+eh)/2
    #         eyewid = eyewid+[ex]
    #         eyewid = eyewid+[ex+ew]
    #     smiles = smileCascade.detectMultiScale(
    #         roi_gray,
    #         scaleFactor=1.2,
    #         minNeighbors=5,
    #         minSize=(50, 130),
    #         maxSize=(100, 200)
    #     )
    #     for (ex,ey,ew,eh) in smiles:
    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    #         mwid=ew
    #         mtop=ey
    #         mbot=ey+eh
    #         mleft = ex
    #         mright = ex+ew
    #         print('MOUTH', "left", ex, "top", ey, "right", ex+ew, "bottom", ey+eh, "width", ew ,"height", eh)
    #     errors = {}
    #     if len(faces) > 1:
    #         errors["faces"] = "Multiple faces detected please take another picture"
    #     if len(faces) < 1:
    #         errors["faces"] = "No faces detected please take another picture"
    #     if len(eyes) > 2:
    #         errors["eyes"] = "More than 2 eyes detected please take another picture"
    #     if len(eyes) < 2:
    #         errors["eyes"] = "Less than 2 eyes detected please take another picture"
    #     if len(smiles) > 1:
    #         errors["smiles"] = "Multiple mouths detected please take another picture"
    #     if len(smiles) < 1:
    #         errors["smiles"] = "No mouths detected please take another picture"
    #     if len(errors):
    #         for key, value in errors.items():
    #             messages.error(request, value)
    #             errors=messages.json(errors)

    #         image = cv2.imwrite('face.jpeg',image)

    #         #context objects to kickback
    #         with open(image, "rb") as image_file:
    #             encoded_string = base64.b64encode(image_file.read())   
    #         context_before = {
    #                 'error': errors,
    #                 'image': encoded_string
    #             }
    #         context = context_before.json(context)
    #         return requests.post('http:local:4200/', context)
    #     else:
    #         #calculations
    #         mofa = mwid/fwid
    #         chinheight = fwid-mbot
    #         hairline = hairline/2
    #         hairtomouth1 = math.atan((mleft-eyewid[0])/(mbot-hairline))*180/math.pi
    #         hairtomouth2 = math.atan((eyewid[3]-mright)/(mbot-hairline))*180/math.pi
    #         chinhypo = (chinheight**2+(mwid/2)**2)**0.5
    #         chinangle = 180 - 2*math.asin(chinheight/chinhypo)*180/math.pi
    #         hairangle = (hairtomouth1+hairtomouth2)/2
    #         print(mofa, chinangle, hairangle,eyewid)

    #         #shape classifier
    #         if (hairangle>16 or hairangle<-16):
    #             if (chinangle<110):
    #                 shape = 'heart'
    #             else:
    #                 shape = 'round'
    #         if (hairangle<=16 and hairangle>=-16):
    #             if (chinangle<110):
    #                 shape = 'diamond'
    #             else:
    #                 if(mofa<0.4):
    #                     shape = 'oval'
    #                 else:
    #                     shape = 'square'

    #         image = cv2.imwrite('face.jpeg',image)

    #         #context objects to kickback
    #         with open(image, "rb") as image_file:
    #             encoded_string = base64.b64encode(image_file.read())   
    #         context_before = {
    #                 'shape': shape,
    #                 'image': encoded_string
    #             }
    #         context = context_before.json(context)
    #         return requests.post('http:local:4200/', context)
    return HttpResponse('it may work')