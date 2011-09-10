
app = Application
prj = app.ActiveProject

#proplist = prj.Properties
#playctrl = proplist("Play Control")

#app.LogMessage( "PlayControl's Name: " + playctrl.Name );
#app.LogMessage( "PlayControl's FullName: " + playctrl.FullName );

for i in range(10):
	Application.SetValue("PlayControl.Current", i, "")
	
	f = open("C:/framespec" + str(i) + ".frs", "w")
	
	furyOptions = app.ActiveProject.ActiveScene.PassContainer.Properties.Filter( "", "", "Exocortex Fury 2 Options" )

	for param in furyOptions(0).Parameters:
		f.write(str(param.Name) + "=" + str(param.Value) + "\n")
	
