# Anleitung für die Verwendung der Dateien

## Wo befinden sich die notwendigen Dateien?
Die notwendigen Dateien sind im Ordner **_Frontend_**. Damit der Chatbot aufgerufen wird, wird die Datei _chatbot2.py_ benötigt. Dort befindet sich das Frontend und die Anbindung zum Backend. Das Backend des Chatbots ist in der Datei *chatbot_model.py* enthalten.

## Welche Bibliotheken möglicherweise benötigt werden
Es gibt im Backend einige Bibliotheken, die für das reibungslose ausführen des Codes notwenidg sind. Ggf. müssten diese installiert werden, falls noch nicht vorhanden.
Folgende Bibliotheken werden benötigt:
  - nltk
  - tensorflow
  - pickle
  - numpy
  - random
  - json
Nach Installation dieser Bibliotheken sollte der Code reibungslos laufen.

## Ablauf
Nachdem die Datei _chatbot2.py_ aufgerufen wird, erscheint in der Console ein Localhost-Link. Diesem können Sie folgen, um im Browser eine Konversation mit dem Chatbot durchzuspielen. Dafür können Sie folgendes ausprobieren:
  - Erstes Beispiel:
      - Beginnen mit: *itching*. Sie können danach entweder *skin rash, nodal skin eruptions, dischromic patches* oder die vom Chatbot vorgeschlagenen Symptome eingeben. Damit müssten Sie die Krankehti *fungal infection* erhalten.
  - Zweites Beispiel:
      - Beginnen mit: *joint pain, neck pain, knee pain*. Gleich wie oben, können Sie entweder *back pain, weakness in limbs, neck pain, loss of balance* eingeben oder die vom Chatbot vorgeschlagenen Symptome. Sie müssten dann *cervical spondylosis* und *fungal infection* mit den dazugehörigen Wahrscheinlichkeiten erhalten.
   - Drittes Beispiel: 
      - Beginnen mit: *fatigue*. Wieder können Sie entweder *throat, high fever, extra marital contacts* oder die vom Chatbot vorgeschlagenen Symptome eingeben. Sie sollten *aids* als Antwort erhalten.
   - Viertes Beispiel:
      - Beginnen mit: *chest pain, dizziness*. Sie geben auch hier entweder *chills, vomiting, fatigue, weight loss, cough, high fever, breathlessness* oder die vorgeschlagenen Symptome ein. Sie erhalten danach als Resultate *fungal infection* und *gastroenteritis*.

## Training-Notebook
Das Notebook, indem alle Schritte des Trainings enthalten sind, finden Sie im Ordner *Frontend*. Die Datei heißt *chatbot_model_keras.ipynb*.
