
app = Application

def exportFramespec(numberOfFrames, outputPath):

	Application.SetValue("PlayControl.Current", 0, "")

	for i in range(numberOfFrames):
		Application.SetValue("PlayControl.Current", i, "")
		
		f = open(outputPath + str(i) + ".frs", "w")
		
		furyOptions = app.ActiveProject.ActiveScene.PassContainer.Properties.Filter("", "", "Exocortex Fury 2 Options")

		for param in furyOptions(0).Parameters:
			f.write(str(param.Name) + "=" + str(param.Value) + "\n")
	
exportFramespec(10, "C:/framespec")