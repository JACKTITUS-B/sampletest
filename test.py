from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def mult():
    a=[[2,3],[4,5]]
    b=[[5,6],[2,4]]
    c=[]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j]=a[i][k]*b[k][j]
    return str(c)
if __name__=="__main__":
    app.run(debug=True)
