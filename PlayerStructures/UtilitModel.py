loaded=loader.loadModel
modeRegist=set()
def torender(model):
    try:
        print(model)
        amodel=NodePath(str(model)+str(len(modeRegist)))
        try:
            rendnodes={each:index for (index,each) in enumerate((render.getChildren()))}
            rendnodes["render/"+model+str(len(modeRegist))]
            print("Not Loaded")
            return 0
        except:
            print("Reparenting to render")
        model.reparentTo(amodel)
        amodel.reparentTo(render)
        modeRegist.add(amodel)
        return amodel
    except Exception as excep:
        print(excep)

def model(loade):
    torender(loaded(loade))





