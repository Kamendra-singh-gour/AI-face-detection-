{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from imageai.Detection import ObjectDetection\n",
    "import os\n",
    "\n",
    "execution_path = os.getcwd()\n",
    "\n",
    "detector = ObjectDetection()\n",
    "detector.setModelTypeAsRetinaNet()\n",
    "detector.setModelPath( os.path.join(execution_path , \"resnet50_coco_best_v2.0.1.h5\"))\n",
    "detector.loadModel()\n",
    "detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , \"image.jpg\"), output_image_path=os.path.join(execution_path , \"imagenew.jpg\"))\n",
    "\n",
    "for eachObject in detections:\n",
    "    print(eachObject[\"name\"] , \" : \" , eachObject[\"percentage_probability\"] )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
