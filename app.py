from flask import Flask, render_template, jsonify
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# Flask Setup
app =  Flask(__name__)

#Database Setup using SQLAlchemy
database_path="titanic.sqlite"
engine=create_engine(f"sqlite:///{database_path}")
Base=automap_base()
Base.prepare(engine,reflect=True)

# Map table
Passengers=Base.classes.passenger

@app.route('/')
def home():

    return render_template("index.html")

@app.route("/statistics/")
@app.route("/statistics/<pclass>")
def statistics(pclass='all'):

    session=Session(engine)
# If pclass is All then query for all male and female passengers and groupby sex and survival status
    if (pclass=='All'):
        result=session.query(Passengers.sex,Passengers.survived,func.count(Passengers.sex)).\
                group_by(Passengers.sex,Passengers.survived).all()
        result_dict=[]
        for sex,survived,count in result:
            stats_dict={}
            stats_dict['sex']=sex
            if (survived==0):
                stats_dict['survived']="no"
            else:
                stats_dict['survived']="yes"
            stats_dict['count']=count
            result_dict.append(stats_dict)   
        session.close()
        return jsonify(result_dict)
    else:
# If pclass is selected then query by class male and female and groupby sex and survival status
        result=session.query(Passengers.sex,Passengers.survived,func.count(Passengers.survived)).\
                        group_by(Passengers.sex,Passengers.survived).\
                        filter(Passengers.pclass==pclass).all()
        result_dict=[]
        for sex,survived,count in result:
            stats_dict={}
            stats_dict['sex']=sex
            if (survived==0):
                stats_dict['survived']="no"
            else:
                stats_dict['survived']="yes"
            stats_dict['count']=count
            result_dict.append(stats_dict)   
        session.close()
        return jsonify(result_dict)
    
if __name__=="__main__":
    app.run(debug=True)